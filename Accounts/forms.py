from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Candidate, Post
from .models import Voter

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class CandidateCreationForm(UserChangeForm):
    class Meta:
        model = User
        fields=['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    post = forms.ModelChoiceField(
    queryset=Post.objects.all(), empty_label=None)
    
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder' : 'Enter password'}), label='Password')

    password2 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder' : 'Confirm Password'}), label='Confirm Password')

class VoterCreationForm(UserChangeForm):
    class Meta:
        model = User
        fields=['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    password1 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder' : 'Enter password'}), label='Password')

    password2 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder' : 'Confirm Password'}), label='Confirm Password')
    