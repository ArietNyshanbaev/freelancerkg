from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Category(models.Model):
	"""Category class which owns skill"""
	

	title = models.CharField(max_length=100)

	def __str__(self):
		return self.title



class Skill(models.Model):
	"""this is class of skills which are is groupped by categories"""
	def __str__(self):
		return self.title +" ==> "+ self.category.title

	category = models.ForeignKey(Category)
	
	title = models.CharField(max_length=200)


	

class Information(models.Model):
	"""This is class which stores all information about particular user"""
	
	def __str__(self):
		return self.user.first_name





	FEMALE = 'F'
	MALE = 'M'


	GENDER_CHOICE = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
	user = models.OneToOneField(User,primary_key=True)
	image = models.ImageField(upload_to = 'media')
	gender = models.CharField(max_length=2,
                                      choices=GENDER_CHOICE,
                                      default=MALE)
	born_date = models.DateField(default=datetime.now, blank=True)
	phone_number = models.IntegerField()
	address = models.CharField(max_length=200,default="Не указано")
	#skills = models.ForeignKey(SkillofUser)


class SkillofUser(models.Model):
	"""docstring for SkillofUser"""
	experience = models.IntegerField()

	skill = models.ForeignKey(Skill)

	BEGINNER = 'BEG'
	INTEMEDIATE = 'INM'
	ADVANCED = 'ADV'
	EXPERT = 'EXP'

	LEVEL_CHOICE = (
		(BEGINNER,'Beginner'),
		(INTEMEDIATE,'Intermediate'),
		(ADVANCED,'Advanced'),
		(EXPERT,'Expert'),
	)

	level = models.CharField(max_length=3,
								choices=LEVEL_CHOICE,
								default=BEGINNER)
	user = models.ForeignKey(Information)

	def __str__(self):
		
		return self.skill.title

		



