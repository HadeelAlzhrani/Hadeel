from django.db import models

# Create your models here.
class User (models.Model):
    user_name=models.CharField(max_length= None)
    email=models.EmailField (null=True)
    passwrd= models.CharField(max_length=20)
    registration_date= models.DateField
    date_of_birth= models.DateField(blank=True, null=True)
    gender= (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    avatar_image=models.ImageField (blank==True, null=True, upload_to="avatar/%Y/%m/%D/")

class Wish (models.Model):
    user_name = models.CharField
    wish= models.CharField(max_length= 140)
    date_and_time= models.DateField(blank=True, null=True)

class Comment (models.Model):
    user_name= models.CharField
    comment_text= models.CharField
    comment_date= models.DateField(blank=True, null=True)


