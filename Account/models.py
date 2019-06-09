from django.db import models

# Create your models here.
class User (models.Model):
    user_name=models.CharField(max_length=20)
    first_name= models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email=models.EmailField (null=True)
    registration_date= models.DateField
    date_of_birth= models.DateField(blank=True, null=True)
    gender_choices = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other')
    )
    gender = models.CharField(
        max_length=1,
        choices=gender_choices,
    )
    avatar_image=models.ImageField (blank=True, null=True, upload_to="avatar/%Y/%m/%D/")

class Wish (models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    description= models.CharField(max_length= 140)
    published_date= models.DateField(auto_now_add=True)

class Comment (models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    wish= models.ForeignKey(Wish, on_delete=models.CASCADE)
    comment_text= models.CharField(max_length=140)
    comment_date= models.DateTimeField(blank=True, null=True)


