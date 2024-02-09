from django import forms
from .models import Profile

class ProfileModelForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Describe yourself!', 'rows': 3}))

    class Meta:
        model = Profile
        fields = ('bio', 'team', 'profile_picture')  # Include 'team' without overriding it
        # Optionally, you can specify widgets for other fields here, excluding 'team'
