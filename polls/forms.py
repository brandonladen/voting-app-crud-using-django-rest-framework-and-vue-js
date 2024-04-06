from Accounts.models import Candidate
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


"""class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class CandidateCreationForm(UserChangeForm):
    full_name = forms.CharField(required=True)
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Password'}), label='Password')
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password'}),label='Confirm Password')
    post = forms.ModelChoiceField(
        queryset=Post.objects.all(), empty_label=None)

    class Meta:
        model = User
        fields=['username','email','password1','password2']"""
"""
class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['post', 'full_name', 'background_info', 'manifesto', 'photo']
"""