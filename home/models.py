import auto_prefetch
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from buyit.utils.managers import CustomUserManager
from buyit.utils.media import profile_image_upload_path
from buyit.utils.models import TimeBasedModel
# from buyit.utils.choices import AddressChoices

class CustomUser(AbstractUser):
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]

    email = models.EmailField(verbose_name="email address", unique=True)
    mobile_no = models.CharField(max_length=15, unique=True, blank=True)
    # mobile_no = PhoneNumberField(blank=True, unique=True)
    profile_pic = models.ImageField(
        upload_to=profile_image_upload_path,
        blank=True,
        verbose_name="Profile Picture",
    )
    objects = CustomUserManager()

    def __str__(self):
        return self.get_full_name() or self.email

    @property
    def image_url(self):

        if self.profile_pic: 
            return self.profile_pic.url

        return f"{settings.STATIC_URL}images/avatars/placeholder.jpg"
    

class Address(TimeBasedModel):
    user = auto_prefetch.ForeignKey(
        'home.CustomUser',
        on_delete=models.CASCADE
    )
    address_line_1 = models.CharField(max_length=150)
    address_line_2 = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    # address_type = models.CharField(
    #     max_length=20,
    #     choices=AddressChoices.choices,
    #     default=AddressChoices.Shipping
    # )
    # default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.address_line_1}, {self.address_line_2}, {self.city}"
    
    class Meta:
        verbose_name_plural = 'Addresses'
    