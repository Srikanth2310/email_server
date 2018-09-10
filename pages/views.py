from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request,*args,**kwargs):
	print(request.user)
	#return HttpResponse("<h1>Welcome to the wrapper!</h1>")
	return render(request,"home.html",{})

def contact_view(*args,**kwargs):
  return HttpResponse("<h1>Wanna contact me?</h1>")

def about_view(request,*args,**kwargs):
  print(request.user)
	#my_context = { 
  #    "my_clg":"BPHC",
  #    "my_degrees":["eco","ece"] 
  #}
  return HttpResponse("<h1>Welcome to non-working About!</h1>")
  #return render(request,"about.html",my_context) 
