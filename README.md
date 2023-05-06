# Huggging Face API Experiments - a project for me to play around with Hugging Face's API
## Language models performance evaluation
Structure and idea stolen from [BabyGPT](https://github.com/Smoothex/BabyGPT).
## Prerequisites
 - At least Python 3.8
 - HuggingFace API key - you can generate one, by [creating an account](https://openai.com/api/), then navigating to Settings > AccessTokens > New token, then save the API key to a file named ```.env``` in a variable called ```HUGGINGFACE_API_KEY```
 - ```pip install python-dotenv``` - allows the application to fetch environmental variables from a .env file
## Basic Method
- Create a script with the type of model you want to use
- Select a [HF model](https://huggingface.co/models)
- Edit request sent to API