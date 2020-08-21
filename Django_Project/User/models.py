from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from Book_store.models import Book
from cart.cart import Cart
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete = models.CASCADE,unique=True)
	name = models.CharField(max_length=64, default=" ")
	image = models.ImageField(default="profile_pic/default.jpg", upload_to = 'profile_pic',null=True)
	def __str__(self):
		return f'{self.user.username} Profile'

class Account(models.Model):
	user = models.OneToOneField(User,related_name="user", null=True, on_delete = models.CASCADE,unique=True)
	def __str__(self):
		return f'{self.user.username} Account'