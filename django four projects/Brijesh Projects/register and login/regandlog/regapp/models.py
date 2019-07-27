from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	father_name = models.CharField(max_length=20, null=True)
	marks = models.CharField(max_length=5, null=True)

	def __str__(self):
		return self.marks

class Games(models.Model):
	
	profile = models.ManyToManyField(Profile)
	gno = models.IntegerField()
	gname = models.CharField(max_length=20)

	def __str__(self):
		return self.gname