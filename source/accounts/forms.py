from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
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


class UserChangePasswordForm(forms.ModelForm):
    password = forms.CharField(max_length=100, required=True, label="Password",
                               widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=100, required=True, label="Password confirm",
                                       widget=forms.PasswordInput)

    old_password = forms.CharField(max_length=100, required=True, label="Old Password ",
                                       widget=forms.PasswordInput)

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        user = self.instance
        if not user.check_password(old_password):
            raise ValidationError('Invalid password', code='invalid_password')
        return old_password


    def clean(self):
        super().clean()
        password_1 = self.cleaned_data.get('password')
        password_2 = self.cleaned_data.get('password_confirm')
        print(password_1 != password_2)
        if password_1 != password_2:
            raise ValidationError('New Password do not match', code='password_do_not_match')
        return self.cleaned_data

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['password', 'password_confirm', 'old_password', ]



