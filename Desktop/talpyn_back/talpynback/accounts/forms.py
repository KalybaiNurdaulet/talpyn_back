# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# You can extend UserCreationForm if you need more fields during registration
# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     class Meta(UserCreationForm.Meta):
#         fields = UserCreationForm.Meta.fields + ('email',)

# For basic registration, UserCreationForm is often enough
# For login, AuthenticationForm is used