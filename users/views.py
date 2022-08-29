from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from users.forms import CreationForm, ProfileForm
from .models import Profile


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("login")
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
            return redirect('users:profile_update')

        context = {'form': form}
        return render(request, self.template_name, context)


class ProfileUpdate(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'users/profile_update.html'
    success_url = reverse_lazy('core:admin_review')

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)
