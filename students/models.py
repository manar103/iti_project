from django.db import models
from tracks.models import Track
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.ImageField(upload_to='students/', null=True, blank=True)
    date_of_birth = models.DateField()
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name