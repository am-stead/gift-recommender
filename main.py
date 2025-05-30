# main.py

import os
import openai
from duckduckgo_search import DDGS
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Agent 1: Generate gift idea + pitch
def get_gift_idea(person_info):
    prompt = f"""
    Suggest a unique gift idea for this person:
    {person_info}

    Also provide a short, fun marketing pitch.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

# Agent 2: Search for product link
def find_product_link(gift_idea):
    with DDGS() as ddgs:
        results = ddgs.text(gift_idea, max_results=1)
        for result in results:
            return result["href"]
    return "No product link found."

# Coordinator: Run the workflow
def run_agentic_gift_recommender(person_info):
    gift_text = get_gift_idea(person_info)
    first_line = gift_text.split("\n")[0]
    product_link = find_product_link(first_line)
    return {
        "gift_idea_and_pitch": gift_text,
        "product_link": product_link
    }

# Run the test workflow
if __name__ == "__main__":
    print("Welcome to the Agentic Gift Recommender!")
    info = input("Describe the person (e.g. age, interests, occasion, etc.):\n> ")

    result = run_agentic_gift_recommender(info)

    print("\n🎁 Gift Idea & Pitch:\n", result["gift_idea_and_pitch"])
    print("\n🔗 Product Link:\n", result["product_link"])
