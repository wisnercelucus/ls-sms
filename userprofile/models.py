from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class BasicDesc(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField(null=True)
	sex = models.CharField(max_length=10)
	phone = models.CharField(max_length=50, null=True)
	mobile = models.CharField(max_length=50)
	city = models.CharField(max_length=50, null=True)
	profile_picture = models.ImageField(upload_to='profile_images', blank=True)
	address = models.CharField(max_length=250, null=True)

	class Meta:
		abstract = True

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	description = models.CharField(max_length=255, null=True)
	city = models.CharField(max_length=250, default='', null=True)
	website = models.URLField(default='', null=True)
	phone = models.IntegerField(default=0, null=True)
	image = models.ImageField(upload_to='profile_images', blank=True, null=True)


	def __str__(self):
		return self.user.username

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)