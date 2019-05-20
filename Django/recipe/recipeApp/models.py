from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    bal="balanced" 
    hp="high-protein"
    hf="high-fiber" 
    lf="low-fat"
    lc="low-carb"
    ls="low-sodium"
    v="vegan"
    veg="vegetarian"
    pal="paleo"
    df="dairy-free"
    gf="gluten-free"
    wf="wheat-free"
    ff="fat-free"
    lsug="low-sugar" 
    ef="egg-free"
    pf="peanut-free"
    tnf="tree-nut-free"
    sf="soy-free"
    fish="fish-free"
    shell="shellfish-free"
    DietChoices = ((bal, "balanced"), (hp, "high-protein"), (hf, "high-fiber"), (lf, "low-fat"), (lc, "low-carb"), (ls, "low-sodium"))
    HealthChoices = ((v, "vegan"), (veg, "vegetarian"), (pal, "paleo"), (df, "dairy-free"), (gf, "gluten-free"), (wf, "wheat-free"), (ff, "fat-free"), (ls, "low-sugar"), 
                     (ef, "egg-free"), (pf, "peanut-free"), (tnf, "tree-nut-free"), (sf, "soy-free"), (fish, "fish-free"), (shell, "shellfish-free"))
    Title = models.CharField(max_length=120) #Recipe Title
    Image = models.FileField(null=True, blank=True) #Optional Image for Recipe
    SourceURL = models.URLField(null=True, blank=True) #Optional URL for original recipe
    Servings = models.IntegerField() #Total number of Servings
    Calories = models.FloatField(null=True, blank=True) #Total number of calories for the recipe
    CaloriesServing = models.FloatField(null=True, blank=True) #Calculated calories per serving (Calories/Servings)
    Diet = models.CharField(max_length=20, choices=DietChoices, default=bal) #Diet restrictions (High-Protein, Low-Fat, etc.)
    Health = models.CharField(max_length=20, choices=HealthChoices, blank=True) #Health food type (Vegan, Gluten Free, etc.)
    Ingredient0 =  models.CharField(max_length=150) 
    Ingredient1 =  models.CharField(max_length=150, blank=True)
    Ingredient2 =  models.CharField(max_length=150, blank=True)
    Ingredient3 =  models.CharField(max_length=150, blank=True)
    Ingredient4 =  models.CharField(max_length=150, blank=True)
    Ingredient5 =  models.CharField(max_length=150, blank=True)
    Ingredient6 =  models.CharField(max_length=150, blank=True)
    Ingredient7 =  models.CharField(max_length=150, blank=True)
    Ingredient8 =  models.CharField(max_length=150, blank=True)
    Ingredient9 =  models.CharField(max_length=150, blank=True)
    Instructions = models.TextField(blank=True) #Coouctions for the recipe

    def __str__(self):
      return self.Title
