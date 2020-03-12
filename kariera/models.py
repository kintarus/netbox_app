from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField


class Miasto(models.Model):
    nazwa = models.CharField(max_length=200)
    kod_pocztowy = models.CharField(max_length=6)
    adres = models.Charfield(max_length=200)

class OfertaPracy(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    foto = models.FileField(upload_to='media/praca', blank=True, null=True)
    zajawka = models.CharField(max_length=120)
    text = RichTextField()
    lokalizacja = models.ManyToManyField(Miasto)
    aktualne = models.BooleanField(default=False, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def published(self):
        self.published_date = timezone.now
        self.save()

    def __str__(self):
        return self.title



