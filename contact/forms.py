
from django.forms import ModelForm

from .models import Contact, Message


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'number']


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['body']
