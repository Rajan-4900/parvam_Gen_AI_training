from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY')
client = genai.Client(api_key=API_KEY)

print("Available models that support generateContent:")
for model in client.models.list():
    if 'generateContent' in model.supported_actions:
        print(f"  {model.name}")