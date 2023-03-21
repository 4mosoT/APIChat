import openai
import os
key = os.environ.get('apikey')
openai.api_key = key


def completion(text):
    r = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f'{text}'},
        ],
    )
    return r
