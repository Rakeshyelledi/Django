from django.db import models

# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length=200)
	rollno = models.CharField(max_length=10)
	branch = models.CharField(max_length=50)


class StudentInfo(models.Model):
	phno = models.CharField(max_length=10)
	emailId = models.EmailField()

	class Meta:
		db_table = 'studentinfo'