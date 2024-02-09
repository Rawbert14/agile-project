from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
from .forms import ProfileModelForm
# Create your views here.

def profile_view(request):
    try: 
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None
    
    form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()  # This saves all the form fields to the model instance
            # Redirect or display a success message here if needed
    
    context = {
        'object': profile,
        'form': form
    }
    
    return render(request, 'profiles/profile.html', context)
