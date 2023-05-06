import json
import requests
import os
from dotenv import load_dotenv
import re

# Set variables
load_dotenv()
API_KEY = os.getenv('HUGGINGFACE_API_KEY')
MODEL_ID = 'gpt2'

# Ask a question
def get_resonse (user_input):
    # Request variables
    headers = {"Authorization": f"Bearer {API_KEY}"}
    API_URL = f'https://api-inference.huggingface.co/models/{MODEL_ID}'
    # Response
    data = json.dumps({'inputs': user_input})
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))[0].get('generated_text')

# Run the chatbot in a loop until the user terminates the programme
while True:
    # Prompt the user to enter a question
    user_input = input("You: ")
    # Check if the user wants to terminate the programme
    if re.search(r"^(exit|quit)$", user_input, re.IGNORECASE):
        print("Chatbot: Goodbye!")
        break
    # Send the user's question to the chatbot and print the bot's response
    print("Chatbot:", get_resonse(user_input))