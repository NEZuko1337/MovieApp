import openai

openai.api_base = "https://api.theb.ai/v1"
openai.api_key = 'sk-17mVUHXC49edx0trRiNXVGhlQi5BSQfHFXgWoinmcs0IV9q3'

completion = openai.ChatCompletion.create(
  model="claude-instant-1",
  messages=[
    {"role": "user", "content": "Можешь посоветовать топ 5 фильмов жанра романтика"}
  ],
  stream=False,
  model_params={
    "temperature": 0.8
  }
)

print(completion.choices[0]['message']['content'])
