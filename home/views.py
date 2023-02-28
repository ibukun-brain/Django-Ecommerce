from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, TemplateView, 
    UpdateView, View
)

from home.forms import UpdateUserForm 
from home.models import CustomUser
from store.models import Order, Payment, Product

# Create your views here.
class IndexView(TemplateView):
    template_name  = 'home/index.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.items.filter(is_available=True) \
            .order_by('-created_at')[:8]
        context["products"] = products
        return context

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'home/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = Order.objects.select_related('user') \
            .filter(user=self.request.user, ordered=True)
        context.update({
            'orders': orders,
            'orders_count': orders.count(),
            })
        return context

class UpdateUserView(LoginRequiredMixin, UpdateView):
    template_name = 'registration/edit-profile.html'
    model = CustomUser
    form_class = UpdateUserForm
    success_url = reverse_lazy('home:edit-profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Profile has been updated successfully')

        return redirect(self.success_url)

class UpdateProfileImageView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):

        user = request.user
        profile_image = request.FILES.get('file')
        success = False
        if profile_image:
            user.profile_pic = profile_image
            user.save()
            success = True

        return JsonResponse({"image_url": user.image_url,"success": success})

class MyorderView(LoginRequiredMixin, ListView):
    template_name = 'home/my_orders.html'
    context_object_name = 'myorders'
    paginate_by = 5

    def get_queryset(self):
        queryset = Order.objects.select_related('user') \
            .filter(user=self.request.user, ordered=True)
        return queryset
    
class MyorderDetailView(LoginRequiredMixin, ListView):
    template_name = 'home/my_order_detail.html'
    context_object_name = 'payment'

    def get_queryset(self):
        order = Order.objects.select_related('user') \
            .get(pk=self.kwargs.get('pk', None))
        queryset = Payment.objects.get(order=order,successful=True)
        return queryset
    
    
# def paginate_my_orderview(request):
#     queryset = Order.objects.select_related('user') \
#             .filter(user=request.user, ordered=True)
#     paginator = Paginator(queryset, 5)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'partials/_my_orders.html', {'page_obj': page_obj})

    