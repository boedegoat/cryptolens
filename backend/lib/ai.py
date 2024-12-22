from openai import OpenAI

client = OpenAI()

def get_ai_completions(**kwargs):
    res = client.chat.completions.create(**kwargs)
    return res.choices[0].message.content