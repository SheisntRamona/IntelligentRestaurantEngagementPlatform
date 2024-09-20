from flask import Flask, request, jsonify, make_response, render_template
from flask_cors import CORS
from config import app
import json
import requests
import time
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
client = OpenAI(
    api_key = os.environ.get('OPENAI_API_KEY'),
)

def CrawlWebsite(url, baseUrl, visitedLinks=None, websiteText='', maxDepth=1, currentDepth=0):
    if visitedLinks is None:
        visitedLinks = set() # initialize as empty if not required
    
    if currentDepth > maxDepth or url in visitedLinks:
        return websiteText

    visitedLinks.add(url)

    # Get the webpage content
    try:
        response = requests.get(url)
        content_type = response.headers.get('content-type')

        if 'application/pdf' not in content_type:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract text from the page
            pageText = soup.get_text(separator=' ', strip=True) #could use (separator=' ', strip=True) to have already parsed text
            print(f"URL: {url}")
            #print(f"Text:\n{pageText[:500]}...")  # Display first 500 characters
            #with open('Dumps/restaurant.txt', 'a') as f:
            #  f.write(pageText)
            #  f.close()
            websiteText += '' + pageText
            print("\n\n")

            # Find all internal links
            for link in soup.find_all('a', href=True):
                href = link['href']
                parsedHref = urlparse(href)

                # Check if the link is an internal link
                if not parsedHref.netloc or parsedHref.netloc == urlparse(baseUrl).netloc:
                    newUrl = urljoin(baseUrl, href)
                    websiteText = CrawlWebsite(newUrl, baseUrl, visitedLinks, websiteText, maxDepth, currentDepth + 1)

    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve {url}: {e}")

    # Pause to avoid overwhelming the server
    time.sleep(0.1)

    return websiteText

class FactPromptGenerator:
    def __init__(self, text, no_facts):
        self.text = text
        self.no_facts = no_facts
        self.system_message = """
            You are tasked with generating a list of facts from text.
            These facts must be truthful and accurate and reflect the information given in the text.
        """
        #The facts should also be quite short, they must be less than 7 words long each.
    def GeneratePrompt(self):
        prompt = f"""
            I am seeking your expertise in distilling key information about text.
            Below I have given text that I have extracted from a certain restaurants website,
            could you please list {self.no_facts} facts about this restaurant.

            {self.text}
        """
        return prompt
    
class QuestionPromptGenerator:
    def __init__(self, facts, no_questions):
        self.facts = facts
        self.no_questions = no_questions
        self.system_message = """
            You are tasked with generating quiz questions about a certain restaurant from a list of facts about that restaurant.
            The questions should have multiple choice answers with one of them marked as correct.
            The other answers should be similar but slightly different from the correct answer to
            mislead a person trying to complete the quiz.
            These questions should be engaging for a customer of the restaurant to answer.
            Please generate the questions in the following JSON format:

            {
                "question": "<insert question>",
                "answers": [
                    {"text": "<answer 1>", "correct": <bool>},
                    {"text": "<answer 2>", "correct": <bool>},
                    {"text": "<answer 3>", "correct": <bool>},
                    {"text": "<answer 4>", "correct": <bool>},
                ]
            }
        """
    def GeneratePrompt(self):
        prompt = f"""
            I am seeking your expertise in generation of quiz questions about a certain restaurant.
            Below, I have given a list of facts about a certain restaurant that I would like you to use in order to generate the quiz questions.

            ---

            Instructions:

            - You must generate {self.no_questions} quiz questions
            - They must be multiple choice
            - They must have the correct answer highlighted
            - Incorrect answers must mislead the quiz participant

            ---

            Facts:

            {self.facts}
        """
        return prompt
    
def ProcessPrompt(promptGen, format={"type": "text"}):
    completion = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": promptGen.system_message},
            {"role": "user", "content": promptGen.GeneratePrompt()}
        ],
        temperature = 0.3,
        max_tokens = 2048,
        response_format = format
    )
    return completion.choices[0].message.content

def generateQuestions():
    startUrl = input("Enter your restaurant's url: ")
    baseUrl = startUrl
    text = CrawlWebsite(startUrl, baseUrl)

    promptGen = FactPromptGenerator(text, 10)
    facts = ProcessPrompt(promptGen)

    promptGen = QuestionPromptGenerator(facts, 5)
    questions = ProcessPrompt(promptGen, {"type": "json_object"})
    return json.loads(questions)

@app.route("/get-questions")
def get_questions():
    return jsonify(questions)

questions = generateQuestions()

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
