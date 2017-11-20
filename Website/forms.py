from django import forms
from .models import *


# Article Form
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'author', 'content')



# Contact Form
class ContactForm(forms.Form):
    contact_firstname = forms.CharField(required=True)
    contact_lastname  = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

# Message Form
class MessageForm(forms.Form):
    class Meta:
        model = Message
        fields = ('sender', 'message', 'origin', 'subject')
