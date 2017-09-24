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