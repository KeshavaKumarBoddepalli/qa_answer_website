import requests

HF_API_KEY = "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"  # Replace with your actual API key

def ask_llm(prompt):
    """Query Hugging Face API for an LLM response."""
    url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 150}
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        return f"Error: {response.json().get('error', 'Unknown error')}"
