from django.db import models

class Student(models.Model):
	firstName = models.CharField(max_length=32)
	lastName = models.CharField(max_length=32)
	numberOfCats = models.IntegerField(default=0)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		self.numberOfCats = self.cat_set.count()
		super().save(*args, **kwargs)

	def __str__(self):
		return self.firstName + " " + self.lastName

class Cat(models.Model):
	name = models.CharField(max_length=32)
	owner = models.ForeignKey(Student, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
