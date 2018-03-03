from django import forms
from .models import *
from Choices import SERVICES

from .models import Message

# Article Form
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'author', 'content')


class MessageForm(forms.Form):
    class Meta:
        model = Message
        fields = "__all__"

#
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'