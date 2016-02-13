"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import *
from ckeditor.fields import RichTextField

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        body = RichTextField()
        fields = ["title", "body"] 

class CommentForm(forms.ModelForm):
    class Meta:
        model = QuestionComment
        question_id = forms.IntegerField()
        fields = ["text"]