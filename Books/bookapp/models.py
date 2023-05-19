from django.db import models

# Create your models here.
class Books(models.Model):
    name=models.CharField(max_length=200)
    year=models.PositiveIntegerField()
    desc=models.TextField()
    img=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name
