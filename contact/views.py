from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import Contact


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated:
            context['contacts'] = Contact.objects.filter(owner=self.request.user)
        return context
