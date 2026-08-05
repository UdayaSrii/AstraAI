from groq import Groq

from config.settings import get_groq_key


api_key = get_groq_key()


if not api_key:

    raise ValueError(
        "GROQ API key missing"
    )


client = Groq(
    api_key=api_key
)



def generate_response(
        messages,
        model,
        temperature,
        max_tokens
):


    response = client.chat.completions.create(

        model=model,

        messages=messages,

        temperature=temperature,

        max_tokens=max_tokens,

        stream=True

    )


    return response