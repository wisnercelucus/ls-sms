from django.db import models

from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from userprofile.models import BasicDesc

from django.conf import settings

# Create your models here.
#fs = FileSystemStorage(location='eSchool/media/documents')

CONTROLS = (
	('controle 1','Controle 1'),
	('controle 2', 'Controle 2'),
	('controle 3','Controle 3'),
	('controle 4','Controle 4'),
	('special control', 'Special control'),
	)

from django.utils import timezone

class TimeStamp(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True



class School(TimeStamp):
	name = models.CharField(max_length=255, null=True)
	acronym = models.CharField(max_length=255, null=True)
	adress = models.CharField(max_length=255, null=True)
	city = models.CharField(max_length=250, default='', null=True)
	responsible_full_name = models.CharField(max_length=255, null=True)
	phone_1 = models.IntegerField(default=0, null=True)
	phone_2 = models.IntegerField(default=0, null=True)
	website = models.URLField(default='', null=True)
	email = models.EmailField(null=True)
	logo = models.ImageField(upload_to='school_images', blank=True, null=True)

	def __str__(self):
		return self.school_name

class AcademicYear(TimeStamp):
	name = models.CharField(max_length=255, null=True)
	start_date = models.DateField(null=True)
	end_date = models.DateField(null=True)

class Document(TimeStamp):
	uploaded_at = models.DateTimeField(auto_now_add=True)
	upload = models.FileField(upload_to='documents')


class Responsible(BasicDesc):
	profession = models.CharField(max_length=255, null=True)
	education_level = models.CharField(max_length=70, null=True)
	reslationshipWithPupil = models.CharField(max_length=250, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	photo = models.ImageField(upload_to='school_images', blank=True, null=True)

	def __str__(self):
		return self.first_name

class Pupil(BasicDesc):
	enrolment_date = models.DateField(null=True)
	birth_date = models.DateField(blank=True, null=True)
	school = models.ForeignKey(School, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)
	photo = models.ImageField(upload_to='school_images', blank=True, null=True)

	def __str__(self):
		return self.first_name

class PupilResponsible(TimeStamp):
	pupil = models.ForeignKey(Pupil, null=True)
	responsible = models.ForeignKey(Responsible, null=True)

class Teacher(BasicDesc):
	academic_level = models.CharField(max_length=250, null=True)
	school = models.ForeignKey(School, null=True)
	status = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	photo = models.ImageField(upload_to='school_images', blank=True, null=True)

	def __str__(self):
		return self.first_name

class Grade(TimeStamp):
	name = models.CharField(max_length=200, null=True)
	description = models.CharField(max_length=255, null=True)

	def __str__(self):
		return self.name

class PupilGradeAtAcademicYear(TimeStamp):
	pupil = models.ForeignKey(Pupil, null=True)
	grade = models.ForeignKey(Grade, null=True)
	academic_year = models.ForeignKey(AcademicYear, null=True)



class Course(TimeStamp):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255, null=True)
	base = models.IntegerField(default=0, null=True)
	coefficient = models.DecimalField(max_digits=6, decimal_places=2, default=0)

	def __str__(self):
		return self.name

class TeachCourseAtSchool(TimeStamp):
	teacher = models.ForeignKey(Teacher, null=True)
	course = models.ForeignKey(Course, null=True)
	School = models.ForeignKey(School, null=True)


class ScoreRecorded(TimeStamp):
	course = models.ForeignKey(Course, null=True)
	pupil = models.ForeignKey(Pupil, null=True)
	academic_year = models.ForeignKey(AcademicYear, null=True)
	score = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
	control = models.CharField(max_length=255, choices=CONTROLS, default='controle 1')


class Attendance(TimeStamp):
	date = models.DateField()
	academic_year = models.ForeignKey(AcademicYear, null=True)
	pupil = models.ForeignKey(Pupil, null=True)
	attended = models.BooleanField(default=True)
	remarks = models.CharField(max_length=255)
	left_early = models.BooleanField(default=True)
	reason_of_leaving = models.CharField(max_length=25, null=True)

# Create your models here.
