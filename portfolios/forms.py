import re
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from portfolios.models import UserProfile

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label='Confirm password',
        widget=forms.PasswordInput()
    )
    # User profile fields:
    latitude = forms.DecimalField()
    longitude = forms.DecimalField()

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2:
            # Only do something if both fields are valid so far.
            if password1 != password2:
                raise forms.ValidationError('Passwords must match.')
            # Always return the full collection of cleaned data.
            return cleaned_data

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Username can only contain alphanumeric '
                                        'characters')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError(u'%s already taken.' % username)

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except ObjectDoesNotExist:
            return email
        raise forms.ValidationError('Email already taken')

    def clean_latitude(self):
        latitude = self.cleaned_data['latitude']
        if latitude > 90 or latitude < -90:
            raise forms.ValidationError('Invalid latitude')
        return latitude

    def clean_longitude(self):
        longitude = self.cleaned_data['longitude']
        if longitude > 180 or longitude < -180:
            raise forms.ValidationError('Invalid longitude')
        return longitude
