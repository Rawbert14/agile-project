from django import forms
from .models import GeneralPost
from django.core.validators import ValidationError

class PostForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    
    class Meta:
        model = GeneralPost
        fields = ('title', 'description', 'image')
        
    def clean_description(self):
        desc = self.cleaned_data.get('description') 
        if len(desc) < 10:
            raise ValidationError("Description too short")
        return desc
        