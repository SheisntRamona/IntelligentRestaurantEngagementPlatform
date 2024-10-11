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

# Load the OpenAI API key
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
    ### Class to generate fact prompt to pass to OpenAI
    def __init__(self, text, no_facts):
        self.text = text
        self.no_facts = no_facts
        self.system_message = """
            You are tasked with generating a list of facts from a lump of text about a restaurant.
            These facts must be truthful and accurate and reflect the information given in the text.
            These facts must also be interesting and unique for a person viewing them and should be styled such
            that they start with "Did you know? blah blah blah".
            Additionally, you must also list the restaurant's name by finding it in the text.

            -------------------------------

            The name and facts need to be in the following format shown inside the double quotes below:

            "Restaurant Name
            Fact
            Fact
            ...
            Fact"

            -------------------------------

            Below is an example of this format shown inside the double quotes

            "Pacific Pines Tavern
            Located in Pacific Pines, QLD, overlooking Central Park.
            Family-friendly hotel with a motto that good food should be shared with good people.
            Offers a spacious bistro known for delicious food, quality service, and comfortable seating. 
            More fact"
        """
    def GeneratePrompt(self):
        prompt = f"""
            I am seeking your expertise in distilling key information about text.
            Below I have given text that I have extracted from a certain restaurants website,
            could you please list {self.no_facts} interesting facts about this restaurant.

            The text you need to list these facts from is in the below double quotes:

            "{self.text}"
        """
        return prompt
    
def ProcessPrompt(promptGen, format={"type": "text"}):
    # Function to process any prompt using gpt-4o-mini
    completion = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": promptGen.system_message},
            {"role": "user", "content": promptGen.GeneratePrompt()}
        ],
        # Keep the model to be fairly deterministic
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