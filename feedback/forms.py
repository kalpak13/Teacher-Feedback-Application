from django import forms
from .models import FeedBack
class FeedbackForm(forms.ModelForm):
    class Meta:
        model=FeedBack
        fields='__all__'
        widgets={"Competency":forms.RadioSelect,
                 "Teaching_Skills":forms.RadioSelect,
                 "Punctuality":forms.RadioSelect, 
                 "Practical_Knowledge":forms.RadioSelect, 
                 "Approachability":forms.RadioSelect, 
                 "Class_Control":forms.RadioSelect,

        }