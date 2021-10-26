from django import forms
from .models import Submission

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['image', 'category', 'public_private', 'date', 'place', 'comment']