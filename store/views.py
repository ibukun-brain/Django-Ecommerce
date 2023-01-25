from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView, FormView, 
    ListView, TemplateView,
    View,
)
from home.models import Address
from store.helpers import get_or_set_order_session
from store.forms import AddToCartForm, AddressForm
from store.models import (
    Order, OrderItem, Category, 
    Product
)
from buyit.utils.choices import AddressChoices

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
        # order_item = None
        if self.request.htmx:
            product = self.get_object()
            order = get_or_set_order_session(self.request)
            order_item = order.orderitem_set.filter(
                product=product,
                # color=form.cleaned_data['color'],
                size=form.cleaned_data['size']
            )
            if order_item.exists():
                order_item = order_item.first()
                order.quantity = int(form.cleaned_data['quantity'])
                # order_item.quantity += int(form.cleaned_data['quantity'])
                order_item.save()

            else:
                order_item = form.save(commit=False)
                order_item.product = product
                order_item.order = order
                order_item.save()

                # return super(ProductDetailView, self).form_valid(form)
            context = {
                'order_item':order_item
            }
            return render(self.request, 'store/partials/_item_quantity.html', context)
    
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        order = Order.objects.get(user=self.request.user)
        order_item = None
        try:
            order_item = OrderItem.objects.get(
            order=order,
            product=self.get_object(),    
        )
        except OrderItem.DoesNotExist:
            pass
        context.update({
            'order_item':order_item,
            'product':self.get_object(
            
            )
        })
        context["product"] = self.get_object()
        return context
    

class CartView(TemplateView):
    template_name = 'store/cart.html'

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
 
        context['order'] = get_or_set_order_session(self.request)
        return context
    

class IncreaseQuantityView(View):

    def get(self, request, *args, **kwargs):
        order_item = get_object_or_404(OrderItem, pk=kwargs['pk'])
        order_item.quantity += 1
        order_item.save()
        context = {'order_item': order_item}
        return render(request, 'store/partials/_item_quantity.html', context=context)
    

class DecreaseQuantityView(View):

    def get(self, request, *args, **kwargs):
        order_item = get_object_or_404(OrderItem, pk=kwargs['pk'])
        if order_item.quantity <= 1:
            order_item.delete()
            return render(request, 'store/partials/_add_to_cart_btn.html')

        else:
            order_item.quantity -= 1
            order_item.save()
        context = {'order_item': order_item}
        return render(request, 'store/partials/_item_quantity.html', context=context)
    

class RemoveOrderItemView(View):
    def get(self, request, *args, **kwargs):
        if request.htmx:
            order_item = get_object_or_404(OrderItem, pk=kwargs['pk'])
            order_item.delete()
            return redirect('store:carts')


class CheckOutView(LoginRequiredMixin, FormView):
    template_name = 'store/checkout.html'
    form_class = AddressForm


    def get_form(self):
        form = super().get_form()
        address = None
        try:
            address = Address.objects.filter(user=self.request.user)[0]
        except Address.DoesNotExist:
            pass
        if address is not None:
            form.fields['address_line_1'].initial = address.address_line_1
            form.fields['address_line_2'].initial = address.address_line_2
            form.fields['city'].initial = address.city
            form.fields['state'].initial = address.state
            form.fields['zip_code'].initial = address.zip_code

        return form

    def form_valid(self, form):
        order = get_or_set_order_session(self.request)
        address, _ = Address.objects.get_or_create(
            user=self.request.user
        )
        address.address_line_1=form.cleaned_data['address_line_1']
        address.address_line_2=form.cleaned_data['address_line_2']
        address.zip_code = form.cleaned_data['zip_code']
        address.city=form.cleaned_data['city']
        address.state=form.cleaned_data['state']
        address.save()
        # address = form.save(commit=False)
        # address.user = self.request.user
        # address.save()
        # if self.request.user == address.user:
        #     address.address_line_1=form.cleaned_data['address_line_1'],
        #     address.address_line_2=form.cleaned_data['address_line_2'],
        #     address.zip_code = form.cleaned_data['zip_code'],
        #     address.city=form.cleaned_data['city'],
        #     address.state=form.cleaned_data['state'],
        # address = Address.objects.create(
        #     user=self.request.user,
        #     address_line_1=form.cleaned_data['address_line_1'],
        #     address_line_2=form.cleaned_data['address_line_2'],
        #     zip_code = form.cleaned_data['zip_code'],
        #     city=form.cleaned_data['city'],
        #     state=form.cleaned_data['state'],
        # )
        order.address = address
        
        order.save()

        messages.info(self.request, 'You have sucessfully added your addresses')
        return redirect(reverse_lazy('home:dashboard'))


    def get_context_data(self, **kwargs):
        context = super(CheckOutView, self).get_context_data(**kwargs)
        context['order'] = get_or_set_order_session(self.request)
        return context
    