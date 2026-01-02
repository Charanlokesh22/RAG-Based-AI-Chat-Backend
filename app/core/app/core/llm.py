from openai import OpenAI
from app.core.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_answer(context: str, question: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Answer using the provided context only."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{question}"}
        ]
    )
    return response.choices[0].message.content
