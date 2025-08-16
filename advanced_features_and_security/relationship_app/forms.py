# django-models/LibraryProject/relationship_app/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    # You can add additional fields here if needed,
    # but for this task, the default UserCreationForm is sufficient.
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',) # Example: Add email field to registration form
        # You can remove ('email',) if you just want username and password