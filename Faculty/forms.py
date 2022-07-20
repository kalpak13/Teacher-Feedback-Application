from django import forms
from .models import Teacher

class NewTeacherForm(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=Teacher

        
        