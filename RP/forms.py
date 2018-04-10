from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Login(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

    def clean(self):
        print(self.cleaned_data.get('email'))
        print(self.cleaned_data)
        return None

    """
    def _clean_fields(self):
        print(self.cleaned_data['email'])
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if User.objects.filter(email__iexact=email, password__iexact=password).exists():
            raise ValidationError("Invalid email or wrong password")
        else:
            return self.cleaned_data
            
                """


