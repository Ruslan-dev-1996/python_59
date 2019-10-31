from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100, required=True,
                              label='Username')
    password = forms.CharField(max_length=100, required=True, label="Password",
                               widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=100, required=True, label="Password confirm",
                               widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=100, required=True, label="First name")
    last_name = forms.CharField(max_length=100, required=True, label="Last name")

    email = forms.EmailField(required=True, label='Email')



    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
            raise ValidationError('Username already taken',  code='username_taken')
        except User.DoesNotExist:
            return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
            raise ValidationError('Email already registered',  code='email_registered')
        except User.DoesNotExist:
            return email


    def clean(self):
        super().clean()
        password_1 = self.cleaned_data.get('password')
        password_2 = self.cleaned_data.get('password_confirm')
        print(password_1 != password_2)
        if password_1 != password_2:
            raise ValidationError('Password do not match', code='password_do_not_match')
        return self.cleaned_data


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']



