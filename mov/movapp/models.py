from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='gallery')
    desc = models.TextField()
    year=models.IntegerField()

    def __str__(self):
        return self.name

