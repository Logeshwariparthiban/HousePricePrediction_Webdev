from django import forms
from .models import *


class ckdForm(forms.ModelForm):
    class Meta():
        model=ckdModel
        fields=['area','bedrooms','bathrooms','stories','parking','mainroad_yes','guestroom_yes', 'basement_yes', 'hotwaterheating_yes', 'airconditioning_yes','prefarea_yes', 'furnishingstatus_semi_furnished', 'furnishingstatus_unfurnished']
