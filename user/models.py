from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(null=False, max_length=18)
    phone = models.IntegerField(null=False)
    email = models.EmailField(null=True, max_length=50)


    def __str__(self):
        return self.name
    


    