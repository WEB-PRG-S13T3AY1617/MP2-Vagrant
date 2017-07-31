from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from .models import Profile

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user is None:
            print("nn")
            raise forms.ValidationError("This user does not exist")
        if user.check_password(password) is None:
            raise forms.ValidationError("Incorrect password")

        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")


    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password2',
        ]

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Passwords must match")


class ProfileForm(forms.ModelForm):
    degoff = forms.CharField(label="Degree or Office")
    class Meta:
        model = Profile
        fields = ['degoff',]
