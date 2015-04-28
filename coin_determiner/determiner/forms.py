from django import forms
from .models import Coin


class CoinForm(forms.ModelForm):
    """
    Write something here
    """

    class Meta:
        model = Coin
        fields = ['value']
