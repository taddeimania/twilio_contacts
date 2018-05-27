
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Contact
from .forms import ContactForm, MessageForm


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated:
            context['contacts'] = Contact.objects.filter(owner=self.request.user)
            context['new_contact_form'] = ContactForm()
        return context


class ContactCreateView(CreateView):
    form_class = ContactForm
    success_url = '/'
    template_name = "contact/contact_create.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ContactDetailView(DetailView):
    model = Contact

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['new_message_form'] = MessageForm()
        return context


class MessageCreateView(CreateView):
    form_class = MessageForm

    def form_valid(self, form):
        contact = Contact.objects.get(id=self.request.POST.get('contact_id', None))
        form.instance.contact = contact
        form.send_sms(contact)
        return super().form_valid(form)
