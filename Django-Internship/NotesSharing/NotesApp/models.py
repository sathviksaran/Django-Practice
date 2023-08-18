from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	v = [
		('d','Select Your gender'),
		('M','Male'),
		('F','Female'),
	]
	p = [
		('G','Guest'),
		('T','Teacher'),
		('S','Student'),
	]
	gd = models.CharField(choices=v,default='d',max_length=5)
	mb = models.CharField(max_length=11)
	uq = models.CharField(max_length=10)
	role = models.CharField(choices=p,default='G',max_length=5)
	is_teacher = models.BooleanField(default=False)
	is_student = models.BooleanField(default=False)
