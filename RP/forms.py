from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Login(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

    def _clean_fields(self):
        email = self.cleaned_data['email'].lower()
        password = self.cleaned_data['password']
        if User.objects.filter(email__iexact=email, password__iexact=password).exists():
            raise ValidationError("Invalid email or wrong password")
        else:
            return self.cleaned_data

