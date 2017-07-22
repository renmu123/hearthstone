from django.db import models
from django.urls import reverse
class Hero(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.CharField(max_length=100)
    contributor = models.CharField(max_length=100)
    ka_name = models.CharField(max_length=100)
    con_time = models.DateTimeField()
    ka_time = models.DateTimeField()
    hero = models.ForeignKey(Hero)
    body = models.TextField(default='')

    def __str__(self):
        return self.ka_name

    def get_absolute_url(self):
        return reverse('hearthstone:detail', kwargs={'pk': self.pk})