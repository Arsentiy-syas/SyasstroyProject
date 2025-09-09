from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model, logout
from django.views.generic import CreateView, UpdateView
from .forms import RegisterUserForm, LoginUserForm, ProfileUserForm
from django.contrib.auth.mixins import LoginRequiredMixin

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name='users/register.html'
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('users:login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Вход пользователя'}


def logout_user(request):
    logout(request)
    return redirect('home')


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    from_class = ProfileUserForm
    fields = ['username']
    template_name = 'users/profile.html'
    extra_context = {'title': 'Профиль'}

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user



