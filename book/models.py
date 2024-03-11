from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.CharField(max_length=50)

    def __str__(self):
        return self.title