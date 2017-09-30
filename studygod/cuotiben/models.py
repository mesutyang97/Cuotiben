from django.db import models

class StudyGroup(models.Model):
	name = models.CharField(max_length = 30)

	def __str__(self):
		return self.name


class User(models.Model):
	name = models.CharField(max_length = 30)
	email = models.CharField(max_length = 30)
	username = models.CharField(max_length = 20)
	pwd = models.CharField(max_length = 30)
	study_group = models.ManyToManyField(StudyGroup)

	def __str__(self):
		return self.name

class Problem(models.Model):
	number = models.IntegerField()
	people = models.ManyToManyField(User)
	name = models.CharField(max_length = 20)
	category = models.CharField(max_length = 30)
	course = models.CharField(max_length = 20)
	school = models.CharField(max_length = 20)
	upload_time = models.DateTimeField()
	year = models.IntegerField()
	study_group = models.ManyToManyField(StudyGroup)
	owner = models.IntegerField()
	solution_number = models.IntegerField()

	def __str__(self):
		return self.name


