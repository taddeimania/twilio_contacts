from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=20)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class Message(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
