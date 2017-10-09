from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import csv
from .models import *
from eSchool.mysettings import args
from .forms import (
	RegistrationForm,
    EditProfileForm,
    PupilForm,
    TeacherForm,
    ResponsibleForm,
    ScoreForm,
    CourseForm,
    AttendanceForm,
    DocumentForm

    )
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
import pandas as pd
from django.urls import reverse_lazy

# Create your views here.




def index(request):
	return render(request, 'school/index.html', args)

def convert_header(csvHeader):
	cols = [ x.replace(' ', '_').lower() for x in csvHeader ]
	return cols

def import_data(request):
	if request.method == 'GET':
		return render(request, 'school/import.html')

	if request.method == 'POST' and request.FILES['myfile']:

		if request.POST.get("object") == '':
			message = 'You may chose an object'
			return render(request, 'school/import.html', {'message': message })

		if request.POST.get("object") == 'Pupil':
			myfile = request.FILES['myfile'] 
			doc = Document()
			doc.upload = myfile
			doc.save()
			print(doc.upload.url)
			if settings.DEBUG == True:
				data = csv.reader(open(doc.upload.path), delimiter=',')
			else:
				data = csv.reader(open(os.path.join(os.getcwd(), myfile)), delimiter=',')
				print(doc.upload.url)
			header = next(data)
			header_cols = convert_header(header)
			i = 0
			k = 0
			for row in data:
				pupil = Pupil()
				for k in range(len(header_cols)):
					row_item = row[k].split(',')
					for item in row_item:
						key = header_cols[k]
						if key == 'responsible':
							item = Responsible.objects.get(pk= int(item))
							#print(item.first_name)
							setattr(pupil, key, item)
						else:
							setattr(pupil, key, item)	
					k +=1
				
				pupil.save()
				i = i + 1
			detailed = 'Sucessfully created '+ str(i) + ' Pupils '
			return render(request,  'school/import_success.html', {'detailed' : detailed })


		if request.POST.get("object") == 'Course':
			myfile = request.FILES['myfile']
			fs = FileSystemStorage(location='eSchool/media/documents')
			filename = fs.save(myfile.name, myfile)
			uploaded_file_url = fs.path(filename)
			data = csv.reader(open(uploaded_file_url), delimiter=',')
			header = next(data)
			header_cols = convert_header(header)
			i = 0
			k = 0
			for row in data:
				course = Course()
				for k in range(len(header_cols)):
					row_item = row[k].split(',')
					for item in row_item:
						key = header_cols[k]
						#print(key)
						if key == 'teacher':
							item = Teacher.objects.get(pk= int(item))
							setattr(course, key, item)
						else:
							setattr(course, key, item)	
					k +=1
				
				course.save()
				i = i + 1
			detailed = 'Sucessfully created '+ str(i) + ' Courses'
			return render(request,  'school/import_success.html', {'detailed' : detailed })

		if request.POST.get("object") == 'Attendance':
			myfile = request.FILES['myfile']
			fs = FileSystemStorage(location='eSchool/media/documents')
			filename = fs.save(myfile.name, myfile)
			uploaded_file_url = fs.path(filename)
			data = csv.reader(open(uploaded_file_url), delimiter=',')
			header = next(data)
			header_cols = convert_header(header)
			i = 0
			k = 0
			for row in data:
				attendance = Attendance()
				for k in range(len(header_cols)):
					row_item = row[k].split(',')
					for item in row_item:
						key = header_cols[k]
						#print(key)
						if key == 'pupil':
							item = Pupil.objects.get(pk= int(item))
							setattr(attendance, key, item)
						else:
							if item == "TRUE" or item == 1:
								item = True
							elif item == "FALSE" or item == 0:
								item = False
							setattr(attendance, key, item)	
					k +=1
				
				attendance.save()
				i = i + 1
			detailed = 'Sucessfully created '+ str(i) + ' attendances'
			return render(request,  'school/import_success.html', {'detailed' : detailed })

		if request.POST.get("object") == 'Responsible':
			myfile = request.FILES['myfile']
			fs = FileSystemStorage(location='eSchool/media/documents')
			filename = fs.save(myfile.name, myfile)
			uploaded_file_url = fs.path(filename)
			data = csv.reader(open(uploaded_file_url), delimiter=',')
			header = next(data)
			header_cols = convert_header(header)
			i = 0
			k = 0
			for row in data:
				responsible = Responsible()
				for k in range(len(header_cols)):
					row_item = row[k].split(',')
					for item in row_item:
						key = header_cols[k]
						setattr(responsible, key, item)	
					k +=1
				responsible.save()
				i = i + 1
			detailed = 'Sucessfully created '+ str(i) + ' responsibles'
			return render(request,  'school/import_success.html', {'detailed' : detailed })

		if request.POST.get("object") == 'Teacher':
			myfile = request.FILES['myfile']
			fs = FileSystemStorage(location='eSchool/media/documents')
			filename = fs.save(myfile.name, myfile)
			uploaded_file_url = fs.path(filename)
			data = csv.reader(open(uploaded_file_url), delimiter=',')
			header = next(data)
			header_cols = convert_header(header)
			i = 0
			k = 0
			for row in data:
				teacher = Teacher()
				for k in range(len(header_cols)):
					row_item = row[k].split(',')
					for item in row_item:
						key = header_cols[k]
						setattr(teacher, key, item)	
					k +=1
				teacher.save()
				i = i + 1
			detailed = 'Sucessfully created '+ str(i) + ' teachers'
			return render(request,  'school/import_success.html', {'detailed' : detailed })


		if request.POST.get("object") == 'Score':
			myfile = request.FILES['myfile']
			fs = FileSystemStorage(location='eSchool/media/documents')
			filename = fs.save(myfile.name, myfile)
			uploaded_file_url = fs.path(filename)
			data = csv.reader(open(uploaded_file_url), delimiter=',')
			header = next(data)
			header_cols = convert_header(header)
			i = 0
			k = 0
			for row in data:
				score = ScoreRecorded()
				for k in range(len(header_cols)):
					row_item = row[k].split(',')
					for item in row_item:
						key = header_cols[k]
						if key == 'pupil_id':
							item = Pupil.objects.get(pk=int(item))
							setattr(score, key, item)
						elif key == 'course_id':
							item = Course.objects.get(pk=int(item))
							setattr(score, key, item)
						setattr(score, key, item)
					k +=1
				score.save()
				i = i + 1
			detailed = 'Sucessfully created '+ str(i) + ' line of academic performances'
			return render(request,  'school/import_success.html', {'detailed' : detailed })

def show_pupil_list(request):
	if request.method == 'GET':
		pupils = Pupil.objects.all()
		site_name = 'CEMMAH'
		form = PupilForm()
		return render(request, 'school/list_pupil.html', { 'site_name': site_name, 'pupils': pupils, 'form': form })
	if request.method == "POST":
		form = PupilForm(data = request.POST)
		if form.is_valid():
			form.save()
			return redirect('school:list_pupil')
		else:
			return redirect('/home/')

def add_new_pupil(request):
	if request.method == 'GET':
		form = PupilForm()
		return render(request, 'school/pupil_form.html', { 'form': form })
	if request.method == 'POST':
		form = PupilForm(data = request.POST)
		if form.is_valid():
			form.save()
			return redirect('school:list_pupil')
		else:
			return redirect('/home/')

def update_pupil(request, id):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	if request.method == 'POST':
		pupil = get_object_or_404(Pupil, id=id)
		form = PupilForm(request.POST or None,  request.FILES or None, instance=pupil)
		if form.is_valid():
			pupil = form.save(commit=False)
			
			pupil.save()
			return redirect('/home/')
	else:
		pupil = get_object_or_404(Pupil, pk=id)
		form = PupilForm(request.POST or None,  request.FILES or None, instance=pupil)	
		context = {
			'form': form,
		}
		return render(request, 'school/pupil_form.html', context)

def show_teacher_list(request):
	if request.method == 'GET':
		teachers= Teacher.objects.all()
		site_name = 'CEMMAH'
		form = TeacherForm()
		context = {'site_name': site_name, 'teachers': teachers, 'form': form}
		return render(request, 'school/list_teacher.html', context)
	else:
		form = TeacherForm(data=request.POST)
		if form.is_valid():
			teacher = form.save(commit=False)
			teacher.save()
			return redirect('school:list_teacher')

def add_new_teacher(request):
	if request.method == 'GET':
		form = TeacherForm()
		return render(request, 'school/teacher_form.html', {'form': form})
	else:
		form = TeacherForm(data=request.POST)
		if form.is_valid():
			teacher = form.save(commit=False)
			teacher.save()
			return redirect('school:list_teacher')


def update_teacher(request, id):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	if request.method == 'POST':
		teacher = get_object_or_404(Teacher, id=id)
		form = TeacherForm(request.POST or None,  request.FILES or None, instance=teacher)
		if form.is_valid():
			teacher = form.save(commit=False)		
			teacher.save()
			return redirect('school:list_teacher')
	else:
		teacher = get_object_or_404(Teacher, pk=id)
		form = TeacherForm(request.POST or None,  request.FILES or None, instance=teacher )	
		context = {
			'form': form,
		}
		return render(request, 'school/teacher_form.html', context)



def show_detail_teacher(request, id):
	teacher = get_object_or_404(Teacher, pk=id)
	return render(request, 'school/show_detail_teacher.html', {'teacher': teacher})

def show_detail_responsible(request, id):
	responsible = get_object_or_404(Responsible, pk=id)
	return render(request, 'school/show_detail_responsible.html', {'responsible': responsible})

def update_responsible(request, id):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	if request.method == 'POST':
		responsible = get_object_or_404(Responsible, id=id)
		form = ResponsibleForm(request.POST or None,  request.FILES or None, instance=responsible)
		if form.is_valid():
			responsible = form.save(commit=False)		
			responsible.save()
			return redirect('school:list_responsible')
	else:
		responsible = get_object_or_404(Responsible, pk=id)
		form = ResponsibleForm(request.POST or None,  request.FILES or None, instance=responsible )	
		context = {
			'form': form,
		}
		return render(request, 'school/responsible_form.html', context)


def add_new_responsible(request):
	if request.method == 'GET':
		form = ResponsibleForm()
		return render(request, 'school/responsible_form.html', { 'form': form })
	if request.method == 'POST':
		form = ResponsibleForm(data = request.POST)
		if form.is_valid():
			form.save()
			return redirect('school:list_responsible')
		else:
			return redirect('/home/')

def show_responsible_list(request):
	if request.method == 'GET':
		form = ResponsibleForm()
		responsibles = Responsible.objects.all()

		site_name = 'CEMMAH'
		context = {'site_name': site_name, 'form': form, 'responsibles': responsibles }
		return render(request, 'school/list_responsible.html', context)
	else:
		form = ResponsibleForm(data = request.POST)
		if form.is_valid():
			responsible = form.save(commit=False)
			responsible.save()
			return redirect('school:list_responsible')

def show_course_list(request):
	if request.method == 'GET':
		form = CourseForm()
		courses = Course.objects.all()
		site_name = 'CEMMAH'
		context = {'site_name': site_name, 'form':form, 'courses':courses }
		return render(request, 'school/list_course.html', context)
	else:
		form = CourseForm(data = request.POST)
		if form.is_valid():
			course = form.save(commit=False)
			course.save()
			return redirect('school:list_course')

def add_new_course(request):
	if request.method == 'GET':
		form = CourseForm()
		return render(request, 'school/course_form.html', { 'form': form })
	if request.method == 'POST':
		form =  CourseForm(data = request.POST)
		if form.is_valid():
			form.save()
			return redirect('school:list_course')
		else:
			return redirect('/home/')

def show_detail_course(request, id):
	course = get_object_or_404(Course, pk=id)
	return render(request, 'school/show_detail_course.html', {'course': course })


def update_course(request, id):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	if request.method == 'POST':
		course = get_object_or_404(Course, id=id)
		form = CourseForm(request.POST or None,  request.FILES or None, instance=course)
		if form.is_valid():
			course = form.save(commit=False)		
			course.save()
			return redirect('school:list_course')
	else:
		course = get_object_or_404(Course, pk=id)
		form = CourseForm(request.POST or None,  request.FILES or None, instance=course )	
		context = {
			'form': form,
		}
		return render(request, 'school/course_form.html', context)

def show_attendance_list(request):
	if request.method == 'GET':
		form = AttendanceForm()
		attendances = Attendance.objects.all()
		site_name = 'CEMMAH'
		context = {'site_name': site_name, 'form': form, 'attendances': attendances }
		return render(request, 'school/list_attendance.html', context)
	else:
		form = AttendanceForm(data= request.POST)
		if form.is_valid():
			attendance = form.save(commit=False)
			attendance.save()
			return redirect('school:list_attendance')

def add_new_attendance(request):
	if request.method == 'GET':
		form = AttendanceForm()
		return render(request, 'school/attendance_form.html', { 'form': form })
	if request.method == 'POST':
		form = AttendanceForm(data = request.POST)
		if form.is_valid():
			form.save()
			return redirect('school:list_attendance')
		else:
			return redirect('/home/')


def show_detail_attendance(request, id):
	attendance = get_object_or_404(Attendance, pk=id)
	return render(request, 'school/show_detail_attendance.html', {'attendance': attendance })

def update_attendance(request, id):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	if request.method == 'POST':
		attendance = get_object_or_404(Attendance, id=id)
		form = AttendanceForm(request.POST or None,  request.FILES or None, instance=attendance)
		if form.is_valid():
			attendance = form.save(commit=False)		
			attendance.save()
			return redirect('school:list_attendance')
	else:
		attendance = get_object_or_404(Attendance, pk=id)
		form = AttendanceForm(request.POST or None,  request.FILES or None, instance=attendance )	
		context = {
			'form': form,
		}
		return render(request, 'school/attendance_form.html', context)

def show_score_list(request):
	if request.method == 'GET':
		form = ScoreForm()
		scores = ScoreRecorded.objects.all()
		site_name = 'CEMMAH'
		context = {'site_name':site_name, 'form': form, 'scores': scores}
		return render(request, 'school/list_score.html', context)
	else:
		form = ScoreForm(data= request.POST)
		if form.is_valid():
			score = form.save(commit=False)
			score.save()
			return redirect('school:list_score')

def add_new_score(request):
	if request.method == 'GET':
		form = ScoreForm()
		return render(request, 'school/score_form.html', { 'form': form })
	if request.method == 'POST':
		form = ScoreForm(data = request.POST)
		if form.is_valid():
			form.save()
			return redirect('school:list_score')
		else:
			return redirect('/home/')

def show_detail_score(request, id):
	score = get_object_or_404(ScoreRecorded, pk=id)
	return render(request, 'school/show_detail_score.html', {'score': score })


def update_score(request, id):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	if request.method == 'POST':
		score = get_object_or_404(ScoreRecorded, id=id)
		form = ScoreForm(request.POST or None,  request.FILES or None, instance=score)
		if form.is_valid():
			score = form.save(commit=False)		
			score.save()
			return redirect('school:list_score')
	else:
		score = get_object_or_404(ScoreRecorded, pk=id)
		form = ScoreForm(request.POST or None,  request.FILES or None, instance=score )	
		context = {
			'form': form,
		}
		return render(request, 'school/score_form.html', context)


def show_detail_pupil(request, id):
	pupil = get_object_or_404(Pupil, pk=id)
	return render(request, 'school/show_detail_pupil.html', {'pupil': pupil })

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
		return render(request, 'pages/change_password.html', args)
