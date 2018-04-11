from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from Owner.models import Owner


class UserForm(forms.ModelForm):

    # if you declear the veribles here you will over write what is in the model.
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    address_1 = forms.CharField(max_length=128, required=False)
    address_2 = forms.CharField(max_length=128, required=False)
    city = forms.CharField(max_length=225, required=False)
    state = forms.CharField(max_length=225, required=False)
    zip_code = forms.CharField(max_length=5, required=False)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
            'address_1',
            'address_2',
            'state',
            'city',
            'zip_code'
        ]

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.exists():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.exists():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=False):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']  # Is this safe, Mo?
        )
        # create user.
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
