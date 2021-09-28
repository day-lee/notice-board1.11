# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    post_edited = models.DateTimeField(auto_now=True)
    post_created = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='upload_files/', max_length=100, null=True, blank=True, default=None)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('board:post-detail', kwargs={'pk': self.pk})
        #return reverse('board:notice-board')

    class Meta:
        ordering = ('post_created',)