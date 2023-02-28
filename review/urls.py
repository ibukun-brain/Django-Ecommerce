from django.urls import path
from review import views as review_views

app_name = 'review'

urlpatterns = [
    path(
        route='dashboard/pending-reviews/',
        view=review_views.ReviewListView.as_view(),
        name='review-list'
    ),
    path(
        route='dashboard/submit-review/<int:pk>/',
        view=review_views.ReviewDetailView.as_view(),
        name='review-detail'
    ),
]
