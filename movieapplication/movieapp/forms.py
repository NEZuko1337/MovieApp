from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from . models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введи свой логин',
        })
    )

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введи пароль',
        })
    )
    
    class Meta:
        model = User
        fields = ('username', 'password')


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder': 'Введите логин',
        })
    )
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите email',
        })
    )

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Введите пароль'
        })
    )

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Повторите пароль'
        })
    )

    photo = forms.ImageField(widget=forms.FileInput(attrs={
        'class' : 'form-control-file'
        }), 
        required=False
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'photo')



class ProfileForm(UserChangeForm):
    photo = forms.ImageField(widget=forms.FileInput(attrs={
        'class' : 'img-fluid',
        })
    )
    class Meta:
        model = User
        fields = ('photo', )

