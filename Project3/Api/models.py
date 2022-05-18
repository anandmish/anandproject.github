
from contextlib import redirect_stderr
from unicodedata import category
from django.shortcuts import redirect, render
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect

# Create your models here.


class Ticket (models.Model):
 Department = models.ForeignKey(User, on_delete=models.CASCADE)
 category = models.TextField(blank=False, max_length=100)
 PWSlab = models.TextField(max_length=100)
 Subject = models.TextField(max_length=100)
 Description = models.TextField(max_length=100)


