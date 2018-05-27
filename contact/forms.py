
from django.forms import ModelForm
from django.conf import settings
from twilio.rest import Client

from .models import Contact, Message


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'number']


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['body']

    def send_sms(self, contact):
        number = contact.number
        client = Client(settings.TWILIO_SID, settings.TWILIO_AUTH)
        body = self.cleaned_data.get('body', 'No Message Provided')

        client.messages.create(
            to="+1" + number,
            from_=settings.TWILIO_NUMBER,
            body=body)
