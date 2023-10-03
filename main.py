import openai
openai.api_key = "zu-51da786a04e4c8e3d7d0c9b354be2017"
openai.api_base = "https://zukijourney.xyzbot.net/v1"


chat_completion = openai.ChatCompletion.create(
    stream=False,
    model="gpt-3.5",
    messages=[
        {
            "role": "user",
            "content": 'Посоветуй фильм в жанре романтика', 
        },
    ],
)
print(chat_completion.choices[0].message.content)