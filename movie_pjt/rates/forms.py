from django import forms
from .models import Movierate, Rate

# Create your models here.

class MovierateForm(forms.ModelForm):

    class Meta:
        model = Movierate
        fields = '__all__'

class RateForm(forms.ModelForm):
    RATE_A, RATE_B, RATE_C, RATE_D, RATE_E = '핵꿀잼', '꿀잼', '낫뱃', '노잼', '핵노잼'
    RATE_CHOICES = [(RATE_A, '핵꿀잼'), (RATE_B, '꿀잼'), (RATE_C, '낫뱃'), (RATE_D, '노잼'), (RATE_E, '핵노잼')]
    star_rate = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(attrs={'class': 'my-rate form-control'}))

    class Meta:
        model = Rate
        fields = ('star_rate',)