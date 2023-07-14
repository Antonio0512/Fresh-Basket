from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'first_name', 'last_name', 'gender', 'profile_picture']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['email'].required = False
        self.fields['gender'].required = False
        self.fields['profile_picture'].required = False

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError("Username is required.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required.")
        return email


class UserRegisterForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')
        field_classes = {
            'username': auth_forms.UsernameField,
        }


class UserLoginForm(auth_forms.AuthenticationForm):
    username = auth_forms.UsernameField(widget=forms.TextInput(attrs={"autofocus": True}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"})
    )

    error_messages = {
        'invalid_login': 'Invalid username or password. Please try again.',
    }


class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'
