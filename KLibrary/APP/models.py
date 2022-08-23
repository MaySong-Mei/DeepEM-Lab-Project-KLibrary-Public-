from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=264, unique=True)
    def __str__(self):
        return "{}-{}".format(self.name,self.email)

class Graph(models.Model):
    name = models.CharField(max_length=40)
    IID = models.CharField(max_length=40)
    reference = models.URLField(max_length=40)
    original_image = models.ImageField()
    data_text = models.FileField(upload_to='GraphDataTXT/')

    # I need to process data here

    def __str__(self):
        return "{}-{}".format(self.name,self.IID)
