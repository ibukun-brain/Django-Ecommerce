from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView, FormView, ListView, TemplateView,
    View,
)
from store.helpers import get_or_set_order_session
from store.forms import AddToCartForm
from store.models import (
    Order, OrderItem, Category, 
    Product
)


# Create your views here.
class ProductListView(ListView):
    template_name = 'store/product_list.html'
    context_object_name = 'products'
    paginate_by = 25
    # allow_empty = True
    ordering = ['-updated_at', '-created_at']

    def get_queryset(self):
        request = self.request
        queryset = Product.items.filter(is_available=True)
        category_slug = request.GET.get('category')
        q = request.GET.get('q')
        if q != None or q == '':
            queryset = queryset.filter(
                Q(name__icontains=q) |
                Q(description__icontains=q)
            ).distinct()

        if category_slug != None or category_slug == '':
            queryset = queryset.filter(categories__slug=category_slug)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.request.GET.get('category')
        context.update(
            {
                'category_slug': category_slug
            }
        )
        return context
    

class ProductDetailView(FormView):
    template_name = 'store/product_detail.html'
    form_class = AddToCartForm
    success_url = reverse_lazy('store:carts')

    def get_object(self):
        return get_object_or_404(
            Product, 
            slug=self.kwargs['slug']
        )
    
    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(ProductDetailView, self).get_form_kwargs(*args, **kwargs)
        kwargs['product_id'] = self.get_object().id
        return kwargs

    def form_valid(self, form):
        order = get_or_set_order_session(self.request)
        product = self.get_object()
        order_filter = order.orderitem_set.filter(
            product=product,
            color=form.cleaned_data['color'],
            size=form.cleaned_data['size']
        )
        if order_filter.exists():
            order = order_filter.first()
            # order.quantity = int(form.cleaned_data['quantity'])
            order.quantity += int(form.cleaned_data['quantity'])
            order.save()

        else:
            new_order_item = form.save(commit=False)
            new_order_item.product = product
            new_order_item.order = order
            new_order_item.save()

        return super(ProductDetailView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context["product"] = self.get_object()
        return context
    

class CartView(TemplateView):
    template_name = 'store/cart.html'

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
 
        context['order'] = get_or_set_order_session(self.request)
        return context

# class CartView(ListView):
#     template_name = 'store/cart.html'
#     context_object_name = 'order'
#     # model = OrderItem

#     def  get_queryset(self):
#         queryset =  get_or_set_order_session(self.request)
#         return queryset

    # def get_context_data(self, **kwargs):
    #     context = super(CartView, self).get_context_data(**kwargs)
    #     context['order'] = get_or_set_order_session(self.request)
    #     return context
    
class IncreaseQuantityView(View):

    def get(self, request, *args, **kwargs):
        order = get_object_or_404(OrderItem, pk=kwargs['pk'])
        order.quantity += 1
        order.save()
        return redirect('store:carts')
    
class DecreaseQuantityView(View):

    def get(self, request, *args, **kwargs):
        order = get_object_or_404(OrderItem, pk=kwargs['pk'])
        if order.quantity <= 1:
            order.delete()
        else:
            order.quantity -= 1
            order.save()
        return redirect('store:carts')
    
class RemoveOrderItemView(View):
    def get(self, request, *args, **kwargs):
        order = get_object_or_404(OrderItem, pk=kwargs['pk'])
        order.delete()
        return redirect('store:carts')

# class AddToCartView(View):

#     def get(self, request, product_id):
#         product = Product.objects.get(id=product_id)
#         cart, _ = Cart.objects.get_or_create(
#             cart_id=get_or_create_session_cart_id(request)
#         )
#         cart_item, created = CartItem.objects \
#             .get_or_create(product=product, cart=cart)
#         if not created:
#             cart_item.quantity += 1
#         cart_item.save()

#         return redirect('store:carts')