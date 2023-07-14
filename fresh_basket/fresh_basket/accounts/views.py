import os

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import generic as generic_views
from django.contrib.auth import views as auth_views, login, logout, get_user_model
from django.contrib.auth import authenticate
from django.urls import reverse_lazy
from django.contrib import messages

from . import forms
from ..promotions.models import Promotions

User = get_user_model()


class UserRegisterView(generic_views.CreateView):
    form_class = forms.UserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('page-home')

    def form_valid(self, form):
        response = super().form_valid(form)

        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)

        return response


class UserLoginView(auth_views.LoginView):
    form_class = forms.UserLoginForm
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse_lazy('page-home')

    def form_invalid(self, form):
        messages.error(self.request, form.error_messages['invalid_login'])
        return super().form_invalid(form)


class UserLogoutView(LoginRequiredMixin, generic_views.View):
    template_name = 'accounts/logout.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        logout(request)
        return redirect('page-home')


class UserDetailsView(LoginRequiredMixin, generic_views.DetailView):
    model = User
    template_name = "accounts/profile-details.html"
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['promotions'] = Promotions.objects.all()
        return context


class UserEditView(LoginRequiredMixin, generic_views.UpdateView):
    model = User
    form_class = forms.UserEditForm
    template_name = 'accounts/profile-edit.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={
            'pk': self.request.user.pk
        })

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        form.save_m2m()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error updating profile.')
        return super().form_invalid(form)


class UserDeleteView(LoginRequiredMixin, generic_views.DeleteView):
    model = User
    template_name = 'accounts/profile-delete.html'
    success_url = reverse_lazy('register')

    def redirect_to_success_url(self):
        return self.success_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_data'] = self.get_object()
        return context

    def form_valid(self, form):
        obj = self.get_object()
        profile_photo_path = None

        if obj.profile_picture and obj.profile_picture.path:
            profile_photo_path = obj.profile_picture.path
            obj.profile_picture.delete()

        obj.delete()

        if profile_photo_path and os.path.isfile(profile_photo_path):
            os.remove(profile_photo_path)

        return super().form_valid(form)
