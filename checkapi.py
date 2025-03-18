# import requests

# HF_API_KEY = "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"
# headers = {"Authorization": f"Bearer {HF_API_KEY}"}

# response = requests.get("https://huggingface.co/api/models")
# if response.status_code == 200:
#     print("✅ API Key is working!")
# else:
#     print("❌ Invalid API Key!")
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch API key from environment variables
HF_API_KEY = os.getenv("HF_API_KEY")

# Hugging Face model URL
MODEL_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"

def ask_llm(prompt):
    """Query the Hugging Face API for an LLM response."""
    if not HF_API_KEY:
        return "Error: API key is missing. Please set HF_API_KEY as an environment variable."

    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {"inputs": prompt, "parameters": {"max_new_tokens": 150}}

    response = requests.post(MODEL_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        return f"Error: {response.json()}"

# Example usage
if __name__ == "__main__":
    prompt = "What is the capital of France?"
    print(ask_llm(prompt))
