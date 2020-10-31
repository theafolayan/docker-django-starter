from django.db import models

# Create your models here.

class Question(models.model):
    question_date = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
