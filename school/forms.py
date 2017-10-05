from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from school.models import *

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User

		fields = (
				'username',
				'first_name',
				'last_name',
				'email',
				'password1',
				'password2'

			)

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()

		return user

		
class EditProfileForm(UserChangeForm):

	class Meta:
		model = User
		fields = (
			'email',
			'first_name',
			'last_name',
			'password'
			)

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
			'course_id',
			'pupil_id',
			'score_first_control',
			'score_second_control',
			'score_third_control',
			'score_fourth_control'

			)

class CourseForm(forms.ModelForm):

	class Meta:
		model = Course
		fields = (
			'name',
			'description',
			'teacher'

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
			'responsible'
			)

class DocumentForm(forms.ModelForm):
	class Meta:
		model = Document
		fields = (
				'upload',
			)