from django.db import models

class StudyGroup(models.Model):
	name = models.CharField(max_length = 30)
	picture = models.ImageField(upload_to = 'studygroups', null = True)
	info = models.CharField(max_length = 30, null = True)

	def __str__(self):
		return self.name


class User(models.Model):
	name = models.CharField(max_length = 30)
	email = models.CharField(max_length = 30)
	username = models.CharField(max_length = 20)
	pwd = models.CharField(max_length = 30)
	study_groups = models.ManyToManyField(StudyGroup)

	def __str__(self):
		return self.name

class Problem(models.Model):
	number = models.ImageField(upload_to = 'problems')
	solution_number = models.ImageField(upload_to = 'solutions')
	people = models.ManyToManyField(User)
	name = models.CharField(max_length = 20)
	category = models.CharField(max_length = 30)
	course = models.CharField(max_length = 20)
	school = models.CharField(max_length = 20)
	source_type = models.CharField(max_length = 20, null =True)
	upload_time = models.DateTimeField()
	year = models.IntegerField()
	study_groups = models.ManyToManyField(StudyGroup)
	owner = models.IntegerField()

	def __str__(self):
		return self.name
