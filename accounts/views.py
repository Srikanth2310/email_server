from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm #use the native Django form
from django.contrib.auth import login, logout

# Create your views here.

#handle signup request
def signup_view(request):
  if request.method=='POST': #Handle POST request
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save() #save to database
      #log the user in
      login(request,user)
      return redirect('accounts:signup')
  else:
    form = UserCreationForm()
  return render(request,'accounts/signup.html',{'form':form})

#Handle login request
def login_view(request):
  if request.method=='POST': #Handle POST request
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      #login the user
      user = form.get_user()
      login(request,user)
      return redirect('accounts:signup')
  else:
    form = AuthenticationForm()    
  return render(request,'accounts/login.html',{'form':form})

#Handle logout request
def logout_view(request):
  if request.method=='POST': #Handle POST request
    logout(request)
    return redirect('accounts:signup')
