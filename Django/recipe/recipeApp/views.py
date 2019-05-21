from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.utils.safestring import mark_safe
from . import forms
from . import models
import json

query = ""

# Create your views here.

#for API URL replace q=best with category to search for
#Replace to=10 with the number of recipes the user would like to search for

def Homepage(request):
  context = {
      "title":"Homepage",
      "header":"Cody Saunders",
      "body":"The goal of this project was to create a website that would allow someone to search for and submit recipes. I learned so much in the process of developing this project. Before this project I had very little experience with web programming and now I feel that I am confident enough to be able create something on my own. In this project I utilized django, html, css, javascript, and websockets. Of all of these I only had previous experience with html and css. I definitely ran into some difficulties along the way in this project and am disappointed that I was unable to implement the use of a third party API that would let users search not only user submitted recipes but an external database as well. However, I am happy with what I have accomplished. I really enjoyed being able to get a working login and submission system working on this site. I was even able to implement a chat system which is something that I definitely wouldn't have even thought to have attempted without this project. Overall, I am much more confident in my web programming skills and am proud of what I have accomplished.",
      "page":"Home",
      "firstURL":"/gallery",
      "firstpage":"Gallery",
      "secondURL":"/recommendation",
      "secondpage":"Recommendation Search",
      "thirdURL":"/submit",
      "thirdpage":"Submit A Recipe",
      "fourthURL":"/chat",
      "fourthpage":"Chat",
      "loginredirect":"/"
      }
  return render(request, 'index.html', context=context)

def Recipe(request, recipe):
  comtext = {
      "title":recipe,
      "page":recipe,
      "firstURL":"/",
      "secondURL":"/recommendation",
      "thirdURL":"/submit",
      "firstpage":"Home",
      "secondpage":"Recommendation Search",
      "thirdpage":"Submit A Recipe",
      "fourthURL":"/chat",
      "fourthpage":"Chat",
      "loginredirect":"/gallery",
      "bgimg":False
      }
  return render(request, recipe.html)

def Gallery(request):
  context = {
      "title":"Gallery",
      "page":"Gallery",
      "firstURL":"/",
      "secondURL":"/recommendation",
      "thirdURL":"/submit",
      "firstpage":"Home",
      "secondpage":"Recommendation Search",
      "thirdpage":"Submit A Recipe",
      "fourthURL":"/chat",
      "fourthpage":"Chat",
      "loginredirect":"/gallery",
      "bgimg":False
      }
  return render(request, "gallery.html", context=context)

def Gallery_Json(request):
  RecipeList = models.Recipe.objects.all()
  responselist = {}
  responselist["Recipes"] = []
  for item in RecipeList:
    responselist["Recipes"]+=[{"Title":item.Title, "SourceURL":item.SourceURL, "Servings":item.Servings, "Calories":item.Calories, "CaloriesServing":item.CaloriesServing, "Diet":item.Diet, "Health":item.Health, "Ingredient0":item.Ingredient0, "Ingredient1":item.Ingredient1, "Ingredient2":item.Ingredient2, "Ingredient3":item.Ingredient3, "Ingredient4":item.Ingredient4, "Ingredient5":item.Ingredient5, "Ingredient6":item.Ingredient6, "Ingredient7":item.Ingredient7, "Ingredient8":item.Ingredient8, "Ingredient9":item.Ingredient9, "Instructions":item.Instructions}]
  return JsonResponse(responselist)

@login_required(login_url="/login/")
def Submit(request):
  if request.method == "POST":
    form_instance = forms.RecipeSubmit(request.POST)
    if form_instance.is_valid():
      CreateRecipe = models.Recipe()
      CreateRecipe.Title = form_instance.cleaned_data["Title"]
      CreateRecipe.Image = form_instance.cleaned_data["Image"]
      CreateRecipe.SourceURL = form_instance.cleaned_data["SourceURL"]
      CreateRecipe.Servings = form_instance.cleaned_data["Servings"]
      CreateRecipe.Calories = form_instance.cleaned_data["Calories"]
      if CreateRecipe.Calories is not None:
        CreateRecipe.CaloriesServing = (CreateRecipe.Calories/CreateRecipe.Servings)
      CreateRecipe.Diet = form_instance.cleaned_data["Diet"]
      CreateRecipe.Health = form_instance.cleaned_data["Health"]
      CreateRecipe.Ingredient0 = form_instance.cleaned_data["Ingredient0"]
      CreateRecipe.Ingredient1 = form_instance.cleaned_data["Ingredient1"]
      CreateRecipe.Ingredient2 = form_instance.cleaned_data["Ingredient2"]
      CreateRecipe.Ingredient3 = form_instance.cleaned_data["Ingredient3"]
      CreateRecipe.Ingredient4 = form_instance.cleaned_data["Ingredient4"]
      CreateRecipe.Ingredient5 = form_instance.cleaned_data["Ingredient5"]
      CreateRecipe.Ingredient6 = form_instance.cleaned_data["Ingredient6"]
      CreateRecipe.Ingredient7 = form_instance.cleaned_data["Ingredient7"]
      CreateRecipe.Ingredient8 = form_instance.cleaned_data["Ingredient8"]
      CreateRecipe.Ingredient9 = form_instance.cleaned_data["Ingredient9"]
      CreateRecipe.Instructions = form_instance.cleaned_data["Instructions"]
      CreateRecipe.save()
      form_instance = forms.RecipeSubmit()
  else:
      form_instance = forms.RecipeSubmit()
  context = {
      "title":"Submit",
      "page":"Submit A Recipe",
      "firstURL":"/",
      "secondURL":"/gallery",
      "thirdURL":"/recommendation",
      "firstpage":"Home",
      "secondpage":"Gallery",
      "thirdpage":"Recommendation Search",
      "fourthURL":"/chat",
      "fourthpage":"Chat",
      "loginredirect":"/submit/",
      "form":form_instance,
      "bgimg":False
      }
  return render(request, 'submit.html', context=context)

@login_required(login_url="/login/")
def Recommendation(request):
  context = {
      "title":"Search",
      "page":"Search",
      "firstURL":"/",
      "firstpage":"Home",
      "secondURL":"/gallery",
      "secondpage":"Gallery",
      "thirdURL":"/submit",
      "thirdpage":"Submit A Recipe",
      "fourthURL":"/char",
      "fourthpage":"chat",
      "bgimg":False,
    }
  return render(request, 'search.html', context=context)

@login_required(login_url="/login/")
# adapted from https://stackoverflow.com/questions/14225601/django-form-to-query-database-models
def Search(request):
  query = request.GET.get('q')
  results = models.Recipe.objects.filter(Title__icontains=query)
  context = {
      "title":"Search",
      "page":"Search",
      "firstURL":"/",
      "firstpage":"Home",
      "secondURL":"/gallery",
      "secondpage":"Gallery",
      "thirdURL":"/submit",
      "thirdpage":"Submit A Recipe",
      "fourthURL":"/char",
      "fourthpage":"chat",
      "bgimg":False,
       "results":results
   }
  return render(request, 'results.html', context=context)

def Chat(request):
  context = {
      "title":"Chat",
      "page":"Chat",
      "firstURL":"/",
      "firstpage":"Home",
      "secondURL":"/recommendation",
      "secondpage":"Recommendation Search",
      "thirdURL":"/submit",
      "thirdpage":"Submit A Recipe",
      "fourthURL":"/gallery",
      "fourthpage":"Gallery",
      "loginredirect":"/chat",
      "bgimg":False
      }
  return render(request, "chat.html", context=context)

def ChatRoom(request, room_name):
  context = {
      "title":room_name,
      "page":"Chat",
      "firstURL":"/",
      "firstpage":"Home",
      "secondURL":"/recommendation",
      "secondpage":"Recommendation Search",
      "thirdURL":"/submit",
      "thirdpage":"Submit A Recipe",
      "fourthURL":"/gallery",
      "fourthpage":"Gallery",
      "loginredirect":"/chat",
      "bgimg":False,
      'room_name_json': mark_safe(json.dumps(room_name))
      }
  return render(request,"room.html", context=context)

def Register(request):
  if request.method == "POST":
    form_instance = forms.RegistrationForm(request.POST)
    if form_instance.is_valid():
      form_instance.save()
      return redirect("/login")
  else:
    form_instance = forms.RegistrationForm()
  context = {
      "form":form_instance,
    }
  return render(request, "registration/register.html", context=context)

def Logout(request):
  logout(request)
  return redirect("/login")
