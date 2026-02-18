import os
from openai import OpenAI
from dotenv import load_dotenv

# .env
load_dotenv()

# client openai
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm(prompt: str, model: str = "gpt-4") -> str:
    """
    promt -> llm
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant for bioequivalence study planning."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3  
        )
        return response.choices[0].message.content
    except Exception as e:
        # zagluwka
        print(f"Error calling LLM: {e}")
        return "Error: Could not get response from LLM."

