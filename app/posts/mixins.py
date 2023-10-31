from django import forms
from profiles.models import Profile

class FormUserRequiredMixin(object):
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            profile = Profile.objects.get(user=self.request.user)
            form.instance.author = profile
            return super(FormUserRequiredMixin, self).form_valid(form)
        else:
            form.add_erro(None, "user must be logged in")
            self.form_invalid(form)