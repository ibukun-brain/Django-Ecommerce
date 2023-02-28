from django import forms
from buyit.utils.forms import CssForm
from review.models import Review


class ReviewForm(forms.ModelForm, CssForm):

    class Meta:
        model = Review
        fields = ['review_title','comment']

        widgets ={
            'review_title':forms.TextInput(
            attrs={
            'placeholder':'e.g I love / I like it'
            }
            )
        }