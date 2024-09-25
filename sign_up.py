from flask import request, jsonify
from config import app, db
from models import FactList
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

            -------------------------------

            The name and facts need to be in the following format:

            Restaurant Name
            Fact
            Fact
            ...
            Fact

            Below is an example of this

            Pacific Pines Tavern
            Random fact about pacific pines tavern blah blah 
            Another random fact
            a third random fact
            More fact
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

def GenerateFacts():
    with app.app_context():
        db.create_all()

        # User enters URL
        startUrl = input("Enter your restaurant's URL:")
        baseUrl = startUrl

        # Crawling website to get text
        text = CrawlWebsite(startUrl, baseUrl)

        # Generate facts and restaurant name from gpt4o-mini
        promptGen = FactPromptGenerator(text, 10)
        facts = ProcessPrompt(promptGen)

        # Formatting the fact list into database format
        facts = facts.strip().split('\n')
        restaurant_name = facts[0]
        facts = facts[1:]
        new_fact_list = FactList(restaurant_name=restaurant_name, facts=facts)

        # Add the new fact list to the database
        db.session.add(new_fact_list)
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        # User enters URL
        startUrl = input("Enter your restaurant's URL:")
        baseUrl = startUrl

        # Crawling website to get text
        text = CrawlWebsite(startUrl, baseUrl)

        # Generate facts and restaurant name from gpt4o-mini
        promptGen = FactPromptGenerator(text, 10)
        facts = ProcessPrompt(promptGen)

        # Formatting the fact list into database format
        facts = facts.strip().split('\n')
        restaurant_name = facts[0]
        facts = facts[1:]
        new_fact_list = FactList(restaurant_name=restaurant_name, facts=facts)

        # Add the new fact list to the database
        db.session.add(new_fact_list)
        db.session.commit()