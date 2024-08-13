from decouple import config
from openai import OpenAI

client = OpenAI(api_key=config("OPENAI_API_KEY"))


def completions(message: str, promt: str, model: str = "gpt-4o-mini") -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": promt},
            {"role": "user", "content": message},
        ],
    )

    return response.choices[0].message.content
