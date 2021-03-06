from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    number = models.CharField(max_length=20, validators=[RegexValidator(regex=r'^\d{10}$')])
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


class Message(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self, *args, **kwargs):
        return reverse('contact_detail_view', args=[self.contact.pk])


