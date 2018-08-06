from django import forms

class RecipeForm(forms.Form):
    recipe_name = forms.CharField(max_length=30)
    servings = forms.IntegerField()
    prep_time = forms.IntegerField() # maybe need to show that it's minutes somehow
    cook_time = forms.IntegerField()
    ingredients = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Example: 1) Five Apples'
    )
    directions = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Example: 1) Preheat the oven to 200 degrees'
    )

    def clean(self):
        cleaned_data = super(RecipeForm, self).clean()
        recipe_name = cleaned_data.get('recipe_name')
        ingredients = cleaned_data.get('ingredients')
        directions = cleaned_data.get('directions')
        servings = cleaned_data.get('servings')
        prep_time = cleaned_data.get('prep_time')
        cook_time = cleaned_data.get('cook_time')
        if not recipe_name or not ingredients or not directions or not servings or not prep_time or not cook_time:
            raise forms.ValidationError('Please enter text in all required fields!')
  
class TimepointForm(forms.Form):
     date = forms.DateField()
     story = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='How did you change your family recipe? Write your story here.'
     )
      
     def clean(self):
        cleaned_data = super(TimepointForm, self).clean()       
        date = cleaned_data.get('date')
        story = cleaned_data.get('story')
        if not date or not story:
            raise forms.ValidationError('Please enter text in all required fields!')
            
class TimelineForm(forms.Form):
    dish_name = forms.CharField(max_length=30)
    
    def clean(self):
        cleaned_data = super(TimelineForm, self).clean()       
        dish_name = cleaned_data.get('dish_name')
        if not dish_name:
            raise forms.ValidationError('Please enter text in all required fields!')
            
      