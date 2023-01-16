from django import forms
from .models import OrderItem, Product
from buyit.utils.forms import CssForm

class AddToCartForm(CssForm, forms.ModelForm):
    size = forms.ModelChoiceField(
        queryset=OrderItem.objects.none(),
        widget=forms.RadioSelect(),
        required=False,        
    )
    color = forms.ModelChoiceField(
        queryset=OrderItem.objects.none(),
        widget=forms.RadioSelect(),
        required=False,
    )

    class Meta:
        model = OrderItem
        fields = ['quantity', 'size', 'color']


    def __init__(self, *args, **kwargs):
        product_id = kwargs.pop('product_id')
        product = Product.objects.get(id=product_id)

        super(AddToCartForm, self).__init__(*args, **kwargs)

        self.fields['color'].queryset = product.available_colors.all()
        self.fields['size'].queryset = product.available_sizes.all()

