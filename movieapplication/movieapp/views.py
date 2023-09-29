from django.shortcuts import render
import openai

openai.api_base = "https://api.theb.ai/v1"
openai.api_key = 'sk-17mVUHXC49edx0trRiNXVGhlQi5BSQfHFXgWoinmcs0IV9q3'


def home(request):
    return render(request, 'movieapp/home.html')


def advice_film(request):
    if request.method == 'POST':
        UserText = request.POST.get('userimport', '')
        if UserText is not '':
            completion = openai.ChatCompletion.create(
            model="claude-instant-1",
            messages=[
                {"role": "user", "content": UserText}
            ],
            stream=False,
            model_params={
                "temperature": 0.8
                }
            )
            advice = completion.choices[0]['message']['content']
            return render(request, 'movieapp/advice_film.html', {
                'advice' : advice
                } 
            )
        else:
            return render(request, 'movieapp/advice_film.html', {
                'error': "Ты ничего не ввел, введи условно жанр, или любую другую информацию, которая тебе интересна"
            }
        )
    else:
        return render(request, 'movieapp/advice_film.html')