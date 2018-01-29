from django import forms
from .models import *
from Choices import SERVICES

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
    contact_phone = forms.IntegerField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    contact_options = forms.CharField(max_length=2)


# Message Form
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

        
        
        
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'