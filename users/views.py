from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from users.forms import CreationForm, ProfileForm
from .models import Profile


class SignUp(SuccessMessageMixin, CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("users:login")
    success_message = 'Вы успешно зарегистрировались, пожалуйста войдите и заполните профиль в личном кабинете.'
    template_name = "users/signup.html"


class ProfileCreate(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('core:home')

    def post(self, request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(self.request, "Профиль успешно создан, после оплаты "
                                           "Вам будет доступен весь функционал в личном кабинете.")
            return redirect(self.success_url)
        context = {'form': form}
        return render(request, self.template_name, context)


class ProfileUpdate(SuccessMessageMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'users/profile_update.html'
    success_message = 'Профиль успешно обновлен!'
    success_url = reverse_lazy('core:home')

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)
