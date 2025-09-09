from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']
        

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите никнейм'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}))
    remember_me = forms.BooleanField(label='Запомнить меня', required=False, widget=forms.CheckboxInput({'class': 'form-check-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'remember_me']


class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Никнейм', widget=forms.TextInput(attrs={'class': 'form-input'}))
