from django.urls import path, include

from .views import *

app_name = 'account'

urlpatterns = [
    path('signup/', sign_up, name='signup_home'),
    path('logout/', logout_view, name='logout_home'),
]
