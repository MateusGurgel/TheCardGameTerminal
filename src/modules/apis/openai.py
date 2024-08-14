from decouple import config
from openai import OpenAI

client = OpenAI(api_key=config("OPENAI_API_KEY"))


def structured_completion(
    message: str, promt: str, response_format: type, model: str = "gpt-4o"
) -> type:
    response = client.beta.chat.completions.parse(
        model=model,
        messages=[
            {"role": "system", "content": promt},
            {"role": "user", "content": message},
        ],
        response_format=response_format,
    )
    return response.choices[0].message.parsed


def completions(message: str, promt: str, model: str = "gpt-4o") -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": promt},
            {"role": "user", "content": message},
        ],
    )

    return response.choices[0].message.content
