from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Post(models.Model):
    title = models.CharField(max_length=255)
    #Al conectar con modelo User, se puede preguntar cualquier cosa de ciho objeto
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title_tag = models.CharField(max_length=255)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        print(self.id)
        return '/article/%s' %(self.id)
