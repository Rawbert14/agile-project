from django import forms
from .models import Profile

class ProfileModelForm(forms.ModelForm):
    
    bio = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Describe yourself!', 'rows': 3,}))
    team = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your team',}))
    
    class Meta:
        model = Profile
        fields = ('bio', 'team', 'profile_picture')