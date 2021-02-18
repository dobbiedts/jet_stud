from django.db import models

# Create your models here.
class student(models.Model):
    stud_no = models.CharField(max_length = 10, help_text = "Enter student number", default = None)
    first_name = models.CharField(max_length = 20, help_text = "Enter first name", default = None)
    last_name = models.CharField(max_length = 20, help_text = "Enter last name")
    class_no = models.CharField(max_length = 10, help_text = "Enter class number")
    age = models.IntegerField(help_text = "enter student age", default = "none")
    
    def __str__(self):
        return self.stud_no
        return self.first_name
        return self.last_name
        return self.class_no
        return self.age
        
        
    
    
    
