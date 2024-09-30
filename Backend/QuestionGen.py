from flask import Flask, request, jsonify, make_response, render_template
from flask_cors import CORS
from config import app, db
from models import FactList
from sign_up import ProcessPrompt
import json
import requests
import time
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import func

_ = load_dotenv(find_dotenv())
client = OpenAI(
    api_key = os.environ.get('OPENAI_API_KEY'),
)
    
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

@app.route("/get-questions/<string:restaurant_name>", methods=["GET"])
def get_questions(restaurant_name):
    normalized_name = restaurant_name.replace(" ", "").lower()

    fact_list = FactList.query.filter(
        func.replace(func.lower(FactList.restaurant_name), " ", "").ilike(f"%{normalized_name}%")
    ).first()

    if not fact_list:
        return jsonify({"message": "Restaurant not found"}), 404

    name = fact_list.restaurant_name
    facts = fact_list.facts

    promptGen = QuestionPromptGenerator(facts, 5)
    questions = ProcessPrompt(promptGen, {"type": "json_object"})
    questions = json.loads(questions)

    return jsonify(questions)

@app.route("/get_fact_list/<string:restaurant_name>", methods=["GET"])
def get_fact_list(restaurant_name):
    fact_list = FactList.query.filter_by(restaurant_name=restaurant_name).one_or_none()

    if not fact_list:
        return jsonify({"message": "Restaurant not found"}), 404
    
    name = fact_list.restaurant_name
    facts = fact_list.facts

    print(name)
    print(facts)

    return jsonify({
        "restaurant_name": name,
        "facts": facts
    }), 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True, use_reloader=False)
