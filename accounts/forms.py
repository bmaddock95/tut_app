from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.forms.widgets import CheckboxSelectMultiple
from django.forms import MultipleChoiceField
from django import forms

class CustomUserCreationForm(UserCreationForm):
    
    days_available = forms.MultipleChoiceField(
		choices=CustomUser.DAY_OPTIONS, 
		widget=forms.CheckboxSelectMultiple()
	)
    
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            "year",
            "email", 
            "username",
            "subject",
            "days_available",
            "hours",
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_days(self.cleaned_data['days_available'])  # Save selected days
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):

    days_available = MultipleChoiceField(
        choices = CustomUser.DAY_OPTIONS,
        widget = CheckboxSelectMultiple()
    )
      
    class Meta:
        model = CustomUser
        fields = (
            "username", 
            "email", 
            "year",
            "subject",
            "days_available",
            "hours",
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_days(self.cleaned_data['days_available'])  # Save selected days
        if commit:
            user.save()
        return user
