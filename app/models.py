from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    deadline = models.DateField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name