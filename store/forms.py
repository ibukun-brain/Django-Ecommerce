from django import forms
from .models import OrderItem
from buyit.utils.forms import CssForm

class AddToCartForm(forms.ModelForm):

    class Meta:
        model = OrderItem
        fields = ['quantity']