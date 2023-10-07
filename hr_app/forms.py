from django import forms
from hr_app.models import *

class Employeeform(forms.ModelForm):
    class Meta:
        model= Employee
        fields=('__all__')  

class HolidayForm(forms.ModelForm):
    class Meta:
        model = Holiday
        fields = ['date', 'description']
    # Customize the date field widget
    date = forms.DateField(widget= forms.DateInput(attrs={'type': 'date'}))



class NewsForm(forms.ModelForm):
    class Meta:
        model = NewsArticle
        fields = ['heading', 'content']


    
