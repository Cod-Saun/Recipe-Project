from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
            label="Email",
            required=True
            )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        
        def save(self, commit=True):
          user = super(RegistrationForm, self).save(commit=False)
          user.email = self.cleaned_data["email"]
          if commit:
            user.save()
          return user

class RecipeSubmit(forms.Form):
    blank=""
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
    HealthChoices = ((blank, ""),(v, "vegan"), (veg, "vegetarian"), (pal, "paleo"), (df, "dairy-free"), (gf, "gluten-free"), (wf, "wheat-free"), (ff, "fat-free"), (ls, "low-sugar"), 
                     (ef, "egg-free"), (pf, "peanut-free"), (tnf, "tree-nut-free"), (sf, "soy-free"), (fish, "fish-free"), (shell, "shellfish-free"))
    Title = forms.CharField(label='Title', max_length=120)
    Image = forms.FileField(label='Image', required=False)
    SourceURL = forms.URLField(label='Recipe URL', required=False)
    Servings = forms.IntegerField(label='Number of Servings')
    Calories = forms.FloatField(label='Total Calories', required=False)
    Diet = forms.ChoiceField(choices=DietChoices, label='Diet', required=False)
    Health = forms.ChoiceField(choices=HealthChoices, label='Health', required=False)
    Ingredient0 = forms.CharField(label='Ingredient 1', max_length=150)
    Ingredient1 = forms.CharField(label='Ingredient 2', max_length=150, required=False) 
    Ingredient2 = forms.CharField(label='Ingredient 3', max_length=150, required=False)
    Ingredient3 = forms.CharField(label='Ingredient 4', max_length=150, required=False)
    Ingredient4 = forms.CharField(label='Ingredient 5', max_length=150, required=False)
    Ingredient5 = forms.CharField(label='Ingredient 6', max_length=150, required=False)
    Ingredient6 = forms.CharField(label='Ingredient 7', max_length=150, required=False)
    Ingredient7 = forms.CharField(label='Ingredient 8', max_length=150, required=False)
    Ingredient8 = forms.CharField(label='Ingredient 9', max_length=150, required=False)
    Ingredient9 = forms.CharField(label='Ingredient 10', max_length=150, required=False)
    Instructions = forms.CharField(label='Instructions', widget=forms.Textarea)

class RecipeSearch(forms.Form):
    blank=""
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
    HealthChoices = ((blank, ""),(v, "vegan"), (veg, "vegetarian"), (pal, "paleo"), (df, "dairy-free"), (gf, "gluten-free"), (wf, "wheat-free"), (ff, "fat-free"), (ls, "low-sugar"), 
                     (ef, "egg-free"), (pf, "peanut-free"), (tnf, "tree-nut-free"), (sf, "soy-free"), (fish, "fish-free"), (shell, "shellfish-free"))
    Title = forms.CharField(label='Title', max_length=120, required=True)
    Servings = forms.IntegerField(label='Number of Servings', required =False)
    Calories = forms.FloatField(label='Total Calories', required=False)
    Diet = forms.ChoiceField(choices=DietChoices, label='Diet', required=False)
    Health = forms.ChoiceField(choices=HealthChoices, label='Health', required=False)
    Ingredient0 = forms.CharField(label='Ingredient 1', max_length=150, required=False)
    Ingredient1 = forms.CharField(label='Ingredient 2', max_length=150, required=False) 
    Ingredient2 = forms.CharField(label='Ingredient 3', max_length=150, required=False)
    Ingredient3 = forms.CharField(label='Ingredient 4', max_length=150, required=False)
    Ingredient4 = forms.CharField(label='Ingredient 5', max_length=150, required=False)
    Ingredient5 = forms.CharField(label='Ingredient 6', max_length=150, required=False)
    Ingredient6 = forms.CharField(label='Ingredient 7', max_length=150, required=False)
    Ingredient7 = forms.CharField(label='Ingredient 8', max_length=150, required=False)
    Ingredient8 = forms.CharField(label='Ingredient 9', max_length=150, required=False)
    Ingredient9 = forms.CharField(label='Ingredient 10', max_length=150, required=False)
