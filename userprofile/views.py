from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import *
from eSchool.mysettings import args
from .forms import (
	RegistrationForm,
    EditProfileForm,
    )
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy




def profile(request):
	return render(request, 'userprofile/userprofile.html')



def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data= request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/home/')
		else:
			return redirect('/home/change-password')
	else:
		form = PasswordChangeForm(user=request.user)
		args = {'form': form}
		return render(request, 'userprofile/change_password.html', args)
