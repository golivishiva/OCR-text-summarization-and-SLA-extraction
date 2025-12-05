import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def summarize_with_groq(text: str) -> str:
    """
    Send text to Groq API and return a summary.
    """
    if not text or not text.strip():
        return "No text found to summarize."

    if not GROQ_API_KEY:
        return "GROQ_API_KEY is missing. Check your .env file."

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "You summarize text clearly."},
            {"role": "user", "content": f"Summarize this: {text}"}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        data = response.json()

        # Debug print (optional)
        print("\nFULL GROQ RESPONSE:\n", data)

        if "choices" in data and data["choices"]:
            return data["choices"][0]["message"]["content"]
        else:
            # If Groq sends an error object
            return f"Groq Error: {data}"

    except Exception as e:
        return f"Summarization failed: {e}"
