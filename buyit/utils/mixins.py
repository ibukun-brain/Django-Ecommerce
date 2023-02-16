from django.contrib.auth.mixins import AccessMixin
from home.models import CustomUser

from django.shortcuts import redirect

class IsSelf(AccessMixin):
    
    def dispatch(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        user = CustomUser.objects.get(slug=slug)
        if request.user != user:
            # return redirect('users:user-profile', user)
            return redirect('/')
        return super(IsSelf, self).dispatch(request, *args, **kwargs)