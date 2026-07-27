import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_response(message: str) -> tuple[str, str]:
    response = client.responses.create(
        model="gpt-5-mini",
        input=message,
    )

    return response.output_text, "gpt-5-mini"