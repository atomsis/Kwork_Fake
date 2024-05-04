from django import forms
from .models import CustomerProfile, PerformerProfile
from django.contrib.auth.models import User


class CustomerProfileForm(forms.ModelForm):
    # user = forms.CharField(label='User', disabled=True)

    class Meta:
        model = CustomerProfile
        fields = ['name', 'contact_info', 'experience']

    # def clean_user(self):
    #     user_instance = self.instance.user
    #     if user_instance:
    #         return user_instance.username
    #     else:
    #         return 'No user'
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['user'].initial = self.clean_user()




class PerformerProfileForm(forms.ModelForm):
    # user = forms.CharField(max_length=150, disabled=True)
    class Meta:
        model = PerformerProfile
        fields = ['name', 'contact_info', 'experience']
