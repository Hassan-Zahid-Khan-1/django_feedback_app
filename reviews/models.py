from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class feedback(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    roll_no=models.DecimalField( max_digits=7,decimal_places=0)
    student_name=models.TextField(max_length=50)
    student_reviews=models.TextField(max_length=300)
   