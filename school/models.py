from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.

class Document(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(upload_to='documents', blank=True)

class State(models.Model):
    status = models.BooleanField(default=True)

    class Meta:
    	abstract = True

class BasicDesc(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField()
	sex = models.CharField(max_length=10)
	phone = models.CharField(max_length=50)
	mobile = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	profile_picture = models.ImageField(upload_to='profile_images', blank=True)
	address = models.CharField(max_length=250)

	class Meta:
		abstract = True

class Responsible(BasicDesc):
	profession = models.CharField(max_length=255)
	education_level = models.CharField(max_length=70)
	reslationshipWithPupil = models.CharField(max_length=250)

	def __str__(self):
		return self.first_name

class Pupil(BasicDesc, State):
    enrolment_date = models.DateField(null=True)
    birth_date = models.DateField(null=True)
    responsible = models.ForeignKey(Responsible, null=True)


    def __str__(self):
    	return self.first_name


class Teacher(BasicDesc, State):
    academic_level = models.CharField(max_length=250)

    def __str__(self):
    	return self.first_name

class Grade(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=255)

	def __str__(self):
		return self.name


class Course(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=255)
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


	def __str__(self):
		return self.name

class ScoreRecorded(models.Model):
	course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
	pupil_id = models.ForeignKey(Pupil, on_delete=models.CASCADE)
	score_first_control = models.DecimalField(max_digits=6, decimal_places=2)
	score_second_control = models.DecimalField(max_digits=6, decimal_places=2)
	score_third_control = models.DecimalField(max_digits=6, decimal_places=2)
	score_fourth_control = models.DecimalField(max_digits=6, decimal_places=2)
	score_total = models.DecimalField(max_digits=6, decimal_places=2, null=True)

class Attendance(models.Model):
	date = models.DateField()
	pupil = models.ForeignKey(Pupil, on_delete=models.CASCADE)
	attended = models.BooleanField()
	remarks = models.CharField(max_length=255)

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	description = models.CharField(max_length=255)
	city = models.CharField(max_length=250, default='')
	website = models.URLField(default='')
	phone = models.IntegerField(default=0)
	image = models.ImageField(upload_to='profile_images', blank=True)


	def __str__(self):
		return self.user.username

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)