from django.db import models
from Faculty.models import Teacher
# Create your models here.
selection=[('1','1'),
           ('2','2'),
           ('3','3'),
           ('4','4'),
           ('5','5'),
           ('6','6'),
           ('7','7'),
           ('8','8'),
           ('9','9'),
           ('10','10'),

]



class FeedBack(models.Model):        
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE)
    Competency=models.CharField(choices=selection,default=5,max_length=50) 
    Teaching_Skills=models.CharField(choices=selection,default=5,max_length=50)
    Punctuality=models.CharField(choices=selection,default=5,max_length=50) 
    Practical_Knowledge=models.CharField(choices=selection,default=5,max_length=50)
    Approachability=models.CharField(choices=selection,default=5,max_length=50)
    Class_Control=models.CharField(choices=selection,default=5,max_length=50)

    def __str__(self):
        return self.teacher.name

   


    
    # Competency, Teaching Skills, Punctuality, Practical Knowledge, Approachability, Class Control etc.