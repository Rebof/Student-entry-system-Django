from django.db import models
from django.forms import ValidationError

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    major = models.CharField(max_length=100)

    def clean(self):
        
        self.name = self.name.title()
        self.address = self.address.title()
        
        if self.age < 0:
            raise ValidationError('Age cannot be negative.')
        

    def save(self, *args, **kwargs):
        self.full_clean()  # Validate and transform data by calling clean 
        super().save(*args, **kwargs)  # Save the instance to the database

    def __str__(self):
        return self.name
    
