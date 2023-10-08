import openai
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from . models import Films, User
from . forms import LoginForm, SignUpForm, ProfileForm

openai.api_key = "zu-51da786a04e4c8e3d7d0c9b354be2017"
openai.api_base = "https://zukijourney.xyzbot.net/v1"


def home(request):
    return render(request, 'movieapp/home.html')


def topfilms(request):
    films = Films.objects.all()
    return render(request, 'movieapp/top50films.html', {'films' : films})


def more_info_about_film(request, pk_id):
    film = get_object_or_404(Films, pk=pk_id)
    return render(request, 'movieapp/more_film_info.html', {"film" : film})


def advice_film(request):
    if request.method == 'POST':
        UserText = request.POST.get('userimport', '')
        if UserText != '':
            try:
                completion = openai.ChatCompletion.create(
                model="gpt-3.5",
                messages=[
                    {"role": "user", "content": UserText}
                ],
                stream=False,
                model_params={
                    "temperature": 0.8
                    }
                )
                advice = completion.choices[0].message.content
            except openai.APIError:
                return render(request, 'movieapp/advice_film.html', {'error':'Возникла ошибка, попробуй еще раз' })
            
            return render(request, 'movieapp/advice_film.html', {'advice':advice })
        else:
            return render(request, 'movieapp/advice_film.html', {
                'error': "Ты ничего не ввел, введи условно жанр, или любую другую информацию, которая тебе интересна"
            }
        )
    else:
        return render(request, 'movieapp/advice_film.html')



def signupuser(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginuser')
        else:
            return render(request, 'movieapp/registration.html', {'form': form, 'error': form.errors.as_text})
    else:
        form = SignUpForm()
    return render(request, 'movieapp/registration.html', {'form': form})



def loginuser(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'movieapp/loginpage.html', {'form' : form, 'error': form.non_field_errors})
        else:
            return render(request, 'movieapp/loginpage.html', {'form' : form, 'error': form.non_field_errors})
    else:
        form = LoginForm()
    return render(request, 'movieapp/loginpage.html', {'form' : form})


def logoutuser(request):
    logout(request)
    return redirect('home')


def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            return render(request, 'movieapp/profilepage.html', {'form' : form, 'error': 'Something went wrong! Try again.'})
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'movieapp/profilepage.html', {'form': form})