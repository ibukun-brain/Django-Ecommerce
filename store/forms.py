from django import forms
from store.models import OrderItem, Product
from home.models import Address, CustomUser
from buyit.utils.forms import CssForm
from buyit.utils.choices import AddressChoices

class AddToCartForm(CssForm, forms.ModelForm):
    size = forms.ModelChoiceField(
        queryset=OrderItem.objects.none(),
        widget=forms.RadioSelect(),
        required=False,        
    )
    # color = forms.ModelChoiceField(
    #     queryset=OrderItem.objects.none(),
    #     widget=forms.RadioSelect(),
    #     required=False,
    # )

    class Meta:
        model = OrderItem
        fields = ['quantity', 'size']
        # fields = ['quantity', 'size', 'color']


    def __init__(self, *args, **kwargs):
        product_id = kwargs.pop('product_id')
        product = Product.objects.get(id=product_id)

        super(AddToCartForm, self).__init__(*args, **kwargs)

        # self.fields['color'].queryset = product.available_colors.all()
        self.fields['size'].queryset = product.available_sizes.all()


class AddressForm(CssForm, forms.ModelForm):
    
    class Meta:
        model = Address
        fields = ['address_line_1','address_line_2','city',
            'state','zip_code']