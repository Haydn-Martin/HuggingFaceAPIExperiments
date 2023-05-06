import json
import requests
import os
from dotenv import load_dotenv

# Set variables
load_dotenv()
API_KEY = os.getenv('HUGGINGFACE_API_KEY')
MODEL_ID = 'facebook/bart-large-cnn'

# Text to summarise
text_file = open("hugging-face-playground/text-to-summarise.txt", "r", encoding="utf8")
text = text_file.read()
text_file.close()
model_input = text

# Get response
headers = {"Authorization": f"Bearer {API_KEY}"}
API_URL = f'https://api-inference.huggingface.co/models/{MODEL_ID}'
def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))
data = query({
    'inputs': model_input
})

# Print response
print(data[0].get('summary_text'))