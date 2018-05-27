from django.db import models
from django.urls import reverse


class Contact(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=20)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class Message(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self, *args, **kwargs):
        return reverse('contact_detail_view', args=[self.contact.pk])


