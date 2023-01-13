from django.shortcuts import render
from django.views.generic import TemplateView

from store.models import Product

# Create your views here.
class IndexView(TemplateView):
    template_name  = 'home/index.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.items.filter(is_available=True) \
            .order_by('-created_at')[:8]
        context["products"] = products
        return context
