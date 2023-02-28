import auto_prefetch
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.template.defaultfilters import truncatewords
from buyit.utils.models import TimeBasedModel
from buyit.utils.html import rating_to_html
# Create your models here.

class Review(TimeBasedModel):
    user = auto_prefetch.ForeignKey(
        'home.CustomUser',
        on_delete=models.CASCADE
    )
    product = auto_prefetch.ForeignKey(
        'store.Product',
        on_delete=models.CASCADE,
        null=True,
    )
    order = auto_prefetch.ForeignKey(
        'store.Order',
        on_delete=models.CASCADE
    )
    review_title = models.CharField(max_length=100)
    comment = models.TextField(
        max_length=250,
        blank=True,
    )
    stars = models.FloatField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0.5)
        ])
    reviewed = models.BooleanField(default=False)

    # class Meta:
        # constraints = [
        #     models.UniqueConstraint(
        #         fields=['user', 'product'],
        #         name='unique review',
        #         )
        #     ]
        
    @property
    def star_rating(self):
        """Converts number rating to html font awesome icon"""
        return rating_to_html(self.stars, show_rating=False)

    @property
    def preview(self):
        return truncatewords(self.comment, 10)

    def __str__(self):
        return self.review_title
    
