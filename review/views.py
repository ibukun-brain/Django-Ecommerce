from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, UpdateView
from review.models import Review
from review.forms import ReviewForm

# Create your views here.

class ReviewListView(LoginRequiredMixin, ListView):
    template_name = 'review/review_list.html'
    paginate_by  = 10
    context_object_name = 'reviews'
    def get_queryset(self):
        reviews_queryset = Review.objects.select_related('user', 'order','product') \
                .filter(user=self.request.user, order__ordered=True, reviewed=False)
      
        return reviews_queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews_count =  self.object_list.count()
        context.update({
            'reviews_count':reviews_count,
        })
        return context



class ReviewDetailView(LoginRequiredMixin, UpdateView):
    template_name = 'review/partials/_review_detail.html'
    form_class = ReviewForm


    def get_object(self):
        pk =  self.kwargs['pk']
        review = Review.objects.get(pk=pk)

        return review

    def form_valid(self, form):
        review_form = form.save(commit=False)
        review_form.user = self.request.user
        review_form.stars = self.request.POST.get('stars')
        review_form.title = form.cleaned_data['review_title']
        review_form.comment = form.cleaned_data['comment']
        review_form.reviewed = True
        review_form.save()

        reviews_queryset = Review.objects.select_related('user', 'order','product') \
                .filter(user=self.request.user, order__ordered=True, reviewed=False)
        # return render(reverse_lazy('review:review-list'))
        reviews_count =  reviews_queryset.count()
        context = {
            'reviews': reviews_queryset,
            'reviews_count':reviews_count,
        }
        return render(self.request, 'review/partials/_review_list.html',context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'review':self.get_object(),
        }) 
        return context
    