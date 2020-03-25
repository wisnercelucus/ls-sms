from django import forms
from school.models import *

class TeacherForm(forms.ModelForm):

	class Meta:
		model = Teacher
		fields = (
			'first_name',
			'last_name',
			'email',
			'sex',
			'phone',
			'mobile',
			'city',
			'profile_picture',
			'address',
			'academic_level'
			)


class ResponsibleForm(forms.ModelForm):

	class Meta:
		model = Responsible
		fields = (
			'first_name',
			'last_name',
			'email',
			'sex',
			'phone',
			'mobile',
			'city',
			'profile_picture',
			'address',
			'profession',
			'education_level',
			'reslationshipWithPupil'
			)

class ScoreForm(forms.ModelForm):

	class Meta:
		model = ScoreRecorded
		fields = (
			'course',
			'pupil',
			'control',
			'score',
			)

class CourseForm(forms.ModelForm):

	class Meta:
		model = Course
		fields = (
			'name',
			'description',

			)

class AttendanceForm(forms.ModelForm):

	class Meta:
		model = Attendance
		fields = (
			'date',
			'pupil',
			'attended',
			'remarks'

			)

class PupilForm(forms.ModelForm):

	class Meta:
		model = Pupil
		fields = (
			'first_name',
			'last_name',
			'email',
			'sex',
			'phone',
			'mobile',
			'city',
			'profile_picture',
			'address',
			'enrolment_date',
			'birth_date',
			)

class DocumentForm(forms.ModelForm):
	class Meta:
		model = Document
		fields = (
				'upload',
			)