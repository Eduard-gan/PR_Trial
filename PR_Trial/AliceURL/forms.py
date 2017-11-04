from AliceURL.models import ShortURL
from django.forms import ModelForm
from django import forms


class ShortenForm(ModelForm):
    class Meta:
        model = ShortURL
        fields = ['target_link']
        widgets = {'target_link': forms.URLInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Введите ссылку'})}
