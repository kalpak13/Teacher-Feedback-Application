from django.db import models
# Create your models here.
class Teacher(models.Model):
    name=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    profilePicture=models.ImageField(upload_to='pictures',blank=True)

    def __str__(self):
        return self.name
        

        