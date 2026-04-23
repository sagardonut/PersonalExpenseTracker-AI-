
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file")

client = Groq(api_key=API_KEY)


def generate_ai_response(data, analysis):
    prompt = f"""
 You are a strict personal finance assistant.

RULES:
- Be extremely concise
- All amounts are in NPR (Nepalese Rupees)
- No unnecessary explanations
- No storytelling
- No greetings
- No emojis
- No extra questions beyond 2
- Focus only on actionable financial advice

INPUT DATA:
Expense History:
{data}

Analysis:
{analysis}

OUTPUT FORMAT (must follow exactly and end the conversation dont ask any questions ):

Summary:
- 1–2 lines max

Key Insights:
- Bullet points only (max 3)

Problems:
- Bullet points only (max 2)

Advice:
- Bullet points only (max 3)
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content