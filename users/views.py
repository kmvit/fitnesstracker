from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from users.forms import CreationForm, ProfileForm
from .models import Profile


class SignUp(SuccessMessageMixin, CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("core:home")
    success_message = 'Вы успешно авторизовались, пожалуйста заполните профиль в личном кабинете.'
    template_name = "users/signup.html"


class ProfileCreate(SuccessMessageMixin, CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'users/profile.html'
    success_message = 'Профиль успешно создан, после оплаты Вам будет доступен весь функционал.'
    success_url = reverse_lazy('core:home')

    def post(self, request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
        context = {'form': form}
        return render(request, self.template_name, context)


class ProfileUpdate(SuccessMessageMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'users/profile_update.html'
    success_message = 'Профиль успешно обновлен!'
    success_url = reverse_lazy('core:admin_review')

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)
