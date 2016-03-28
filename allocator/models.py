from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
	user_id=models.IntegerField(primary_key=True,null=False)
	email_id=models.CharField(max_length=30)
	firstname=models.CharField(max_length=15)
	lastname=models.CharField(max_length=15)
	date_of_birth=models.DateTimeField(default=timezone.now())
	password=models.CharField(max_length=30)
	skills=models.CharField(max_length=100)
	edu_background=models.CharField(max_length=100)
	interests=models.CharField(max_length=100)
	votes=models.IntegerField(default=0)
	profile_pic_loc=models.CharField(max_length=100)
	participated_pid=models.CharField(default='',max_length=200)
	
	def __str__(self):
		return self.firstname
	
		
class Project(models.Model):
	project_name=models.CharField(max_length=30)
	project_id=models.IntegerField(primary_key=True)
	project_logo=models.CharField(max_length=100)
	date_created=models.DateTimeField(default=timezone.now())
	description=models.CharField(max_length=50)
	category=models.CharField(max_length=30)
	skills_reqd=models.CharField(max_length=100)
	edu_background_reqd=models.CharField(max_length=100)
	payment=models.IntegerField(default=0)
	status=models.CharField(max_length=15)

	def __str__(self):
		return self.project_name
