from django.db import models
from mongoengine import *

# Create your models here.
class Booking(Document):
	# def __init__(self):
	# 	self.rooms = models.ManyToManyField()
	# 	self.expected = models.TextField()
	# 	self.timeRange = models.TextField()
	def __init__(self):
		self.rooms = models.ManyToManyField()
		self.expected = TextField()
		self.timeRange = TextField()
