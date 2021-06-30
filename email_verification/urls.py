from django.urls import path
from .views import (
    send_email,
    verify_email,
    view_user
)


urlpatterns = [   
    path('send/', send_email),
    path('verify/', verify_email, name="email-verify"),
    path('view/', view_user),
    
]