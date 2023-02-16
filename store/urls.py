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
    path(
    route='checkout/',
    view=store_views.CheckOutView.as_view(),
    name='checkout'
    ),
    path(
    route='add_to_cart_btn/',
    view=store_views.AddToCartVariationBtnView.as_view(),
    name='add-to-cart-variation-btn'
    ),
    path(
    route='make-payment/',
    view=store_views.PaymentView.as_view(),
    name='payment',
    ),  
    path(
    route='confirm-order/',
    view=store_views.ConfirmOrderView.as_view(),
    name='confirm-order',
    ),  
    path(
    route='payment-completed/',
    view=store_views.PaymentCompleteView.as_view(),
    name='payment-complete',
    ),
    # path(
    # route='variation_form/',
    # view=store_views.VariationFormView.as_view(),
    # name='variation-form'
    # ),
    
]
