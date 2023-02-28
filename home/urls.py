from django.urls import path
from home import views as home_views

app_name = 'home'

urlpatterns = [
    path(
        '',
        home_views.IndexView.as_view(),
        name='index'
    ),
    path(
        'dashboard/',
        home_views.DashboardView.as_view(),
        name='dashboard'
    ),
    path(
        'dashboard/edit-profile',
        home_views.UpdateUserView.as_view(),
        name='edit-profile'
    ),
    path(
        'dashboard/update-image',
        home_views.UpdateProfileImageView.as_view(),
        name='update-image'
    ),
    path(
        'dashboard/myorders/',
        home_views.MyorderView.as_view(),
        name='myorder'
    ),
    path(
        'dashboard/myorders/<int:pk>/',
        home_views.MyorderDetailView.as_view(),
        name='myorder-detail'
    )
    # path(
    # 'dashboard/paginate-myorders/',
    # home_views.paginate_my_orderview,
    # name='paginate_myorder'
    # ),
]
