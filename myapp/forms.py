from django import forms
from .models import Teachers, StudentsQuery, Feedback

# Teacher Registration Form


class Teacher(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = ['name', 'email', 'phone', 'address', 'subject', 'experience', 'bio']

# Student Query Form


class StudentQueryForm(forms.ModelForm):
    class Meta:
        model = StudentsQuery
        fields = ['name', 'email', 'phone', 'address', 'query']
        
        
    
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'comment']
