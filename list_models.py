import google.generativeai as genai
import os

# Set your API key here
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

models = genai.list_models()
for model in models:
    print(f"Model: {model.name} | Supported Methods: {model.supported_generation_methods}")


