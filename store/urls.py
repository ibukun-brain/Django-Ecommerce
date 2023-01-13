from django.urls import path
from store.models import Product
from store import views as store_views

app_name = 'store'

urlpatterns = [
    path(
        route='',
        view=store_views.ProductListView.as_view(),
        name='product-list'
    ),
    path(
        route='product/<slug:slug>/',
        view=store_views.ProductDetailView.as_view(),
        name='product-detail'
    ),
    path(
        route='carts/',
        view=store_views.CartView.as_view(),
        name='carts'
    ),
    path(
    route='increase-quantity/<int:pk>/',
    view=store_views.IncreaseQuantityView.as_view(),
    name='increase-quantity'
    ),
    path(
    route='decrease-quantity/<int:pk>/',
    view=store_views.DecreaseQuantityView.as_view(),
    name='decrease-quantity'
    ),
    path(
    route='remove-orderitem/<int:pk>/',
    view=store_views.RemoveOrderItemView.as_view(),
    name='remove-orderitem'
    ),
    
]
