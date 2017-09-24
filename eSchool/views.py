from django.shortcuts import render
from .mysettings import args

def index(request):
	return render(request, 'pages/index.html', args)

def handler404(request):
	return render(request, 'errors/404.html', args, status=404)

def handler500(request):
	return render(request, 'errors/500.html', args, status=500)