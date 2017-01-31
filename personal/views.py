from django.shortcuts import render, redirect

def home(request):
	return redirect('/about')

def about(request):
	return render(request, 'personal/about.html')

def resume(request):
	return render(request, 'personal/resume.html')

def contact(request):
	return render(request, 'personal/contact.html')