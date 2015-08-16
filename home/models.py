from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Category(models.Model):
	"""Category class which owns skill"""

	title = models.CharField('категория',max_length=100)
	icon = models.ImageField('иконка', null=True, blank=True)

	def __unicode__(self):
		return self.title
	class Meta:
		verbose_name = "категория"
		verbose_name_plural = "категории"

class Skill(models.Model):
	"""this is class of skills which are is groupped by categories"""
	
	category = models.ForeignKey(Category, verbose_name='категория')
	title = models.CharField('навык', max_length=200)

	def __unicode__(self):
		return self.title +" ==> "+ self.category.title
	
	class Meta:
		verbose_name = "навык"
		verbose_name_plural = "навыки"

class Information(models.Model):
	"""This is class which stores all information about particular user"""
	
	def __unicode__(self):
		return self.user.first_name

	FEMALE = 'F'
	MALE = 'M'

	GENDER_CHOICE = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
	user = models.OneToOneField(User, primary_key=True, verbose_name='пользователь')
	image = models.ImageField('фото', upload_to = 'media', null=True, blank=True)
	gender = models.CharField('пол', max_length=2,
                                      choices=GENDER_CHOICE,
                                      default=MALE)
	born_date = models.DateField('дата рождения', default=datetime.now, blank=True)
	phone_number = models.IntegerField('номер телефона')
	date = models.DateField('дата регистрации', default = datetime.now)
	stuff = models.BooleanField('исполнитель', default=False)
	category = models.ForeignKey(Category, verbose_name='категория')
	note = models.CharField('информация о пользователе', max_length=3000, null=True, blank=True)
	note_for_us = models.CharField('информация о для нас', max_length=3000, null=True, blank=True)
	note_of_pirces = models.CharField('информация о делах и ценах', max_length=3000, null=True, blank=True)
	


	class Meta:
		verbose_name = "анкета"
		verbose_name_plural = "анкеты"

class SkillofUser(models.Model):
	"""docstring for SkillofUser"""
	experience = models.IntegerField('стаж')

	skill = models.ForeignKey(Skill, verbose_name='навык')

	level = models.CharField('уровень навыка', max_length=11)
	user = models.ForeignKey(Information, verbose_name='пользователь')

	def __unicode__(self):
		return self.skill.title + ' ==> ' + self.user.user.username 
	
	class Meta:
		verbose_name = "навык пользователя"
		verbose_name_plural = "навыки пользователей"

class Job(models.Model):
	title = models.CharField('тема', max_length = 200)
	description = models.TextField('описание', null=True, blank=True)
	price = models.IntegerField('цена', null=True, blank=True)
	category = models.ForeignKey(Category, verbose_name='категория')
	date = models.DateTimeField('дата добавления', default=datetime.now)
	user = models.ForeignKey(User,default=None, verbose_name='пользователь')
	address = models.TextField('адрес', null=True, blank=True)

	def __unicode__(self):
		return self.title
	
	class Meta:
		verbose_name = "задание"
		verbose_name_plural = "задания"

class Slogan(models.Model):
	body = models.CharField('цитата', max_length=200)
	def __unicode__(self):
		return self.body

	class Meta:
		verbose_name = "цитата"
		verbose_name_plural = "цитаты"

class Mail(models.Model):
	name = models.CharField('имя отправителя',max_length=100)
	email = models.CharField(max_length=100)
	title = models.CharField('тема',max_length=100)
	body = models.CharField('сообщение',max_length=1000)
	date = models.DateTimeField('дата отправления', default=datetime.now)
	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = "сообщение"
		verbose_name_plural = "сообщения"

class Order(models.Model):
	name = models.CharField('имя заказчика',max_length=100)
	telephone = models.CharField('номер телефона',max_length=100)
	category = models.ForeignKey(Category, verbose_name='категория')
	date_of_order = models.CharField('дата и время исполнения заказа',max_length=200, default="не указан")
	job_description = models.TextField('описание заказа', default="не указан")
	address = models.CharField('номер телефона',max_length=400, default="не указан")
	date_of_submition = models.DateTimeField('дата и время поступления заявки', default=datetime.now)
	def __unicode__(self):
		return self.name + " " + self.telephone

	class Meta:
		verbose_name = "заявка"
		verbose_name_plural = "заявки"
		
