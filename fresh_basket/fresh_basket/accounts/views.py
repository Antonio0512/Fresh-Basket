from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import generic as generic_views
from django.contrib.auth import views as auth_views, login, logout, get_user_model
from django.contrib.auth import authenticate
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import UserCreateForm, UserLoginForm

User = get_user_model()


class UserRegisterView(generic_views.CreateView):
    form_class = UserCreateForm
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
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse_lazy('page-home')

    def form_invalid(self, form):
        messages.error(self.request, form.error_messages['invalid_login'])
        return super().form_invalid(form)


class UserLogoutView(generic_views.View):
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
