from django.db import models

# Create your models here.

class Member(models.Model):
	name = models.CharField(max_length=10)
	memberid = models.CharField(max_length=20)
	password = models.CharField(max_length=16)
	email = models.EmailField()
	birth = models.DateTimeField()
	phone = models.CharField(max_length=11)
	gender = models.CharField(max_length=1)
	tier = models.CharField(max_length=10)
	TS_CREATED = models.DateTimeField()
	TS_UPDATED = models.DateTimeField()
	def __str__(self):
		return self.name

class StockCard(models.Model):
	name = models.CharField(max_length=30)
	information = models.TextField()
	total_score = models.DecimalField(max_digits=3, decimal_places=1)
	def __str__(self):
		return self.name
