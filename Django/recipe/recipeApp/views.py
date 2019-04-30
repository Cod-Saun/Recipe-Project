from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from . import forms
from . import models

# Create your views here.

#for API URL replace q=best with category to search for
#Replace to=10 with the number of recipes the user would like to search for
APIKey=""

def Homepage(request):
  context = {
      "title":"Homepage",
      "body":"Hello",
      "page":"Home"
      }
  return render(request, 'index.html', context=context)

def Recipes(request):
  context = {
      "title":"Recipes",
      "page":"Recipes"
      }
  return render(request, 'recipes.html', context=context)

@login_required(redirect_field_name='/', login_url="/login")
def Recommendation(request):
  context = { 
      "title":"Recipe Recommendation Search",
      "page":"Recommendation"
      }
  return render(request, 'recommendation.html', context=context)

def Register(request):
  if request.method == "POST":
    form_instance = forms.RegistrationForm(request.POST)
    if form_instance.is_valid():
      form_instance.save()
      return redirect("/")
  else:
    form_instance = forms.RegistrationForm()
  context = {
      "form":form_instance,
    }
  return render(request, "registration/register.html", context=context)

def Logout(request):
  logout(request)
  return redirect("/login")
