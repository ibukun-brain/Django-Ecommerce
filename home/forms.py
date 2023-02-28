from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from buyit.utils.forms import CssForm
from home.models import CustomUser

class UpdateUserForm(UserChangeForm, CssForm):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'mobile_no', 'profile_pic']


class SignupForm(UserCreationForm, CssForm):
    first_name = forms.CharField(
        label="First name",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First name',
                'required': True,
            }
        )
    )
    last_name = forms.CharField(
        label="Last name",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last name',
                'required': True,
            }
        )
    )
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password'
            }
        ),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm Password'
            }
        ),
        strip=False,
    )
    class Meta:
        model = CustomUser
        fields = [
                'first_name',
                'last_name',
                'email',
                'mobile_no',
                'username',
                'password1',
                'password2'
            ]


        widgets = {  
            'email': forms.EmailInput(
                attrs={
                'placeholder': 'Email address',
            }),
            'username': forms.TextInput(
                attrs={
                'placeholder': 'Username',
            }),
        }