from django.urls import path
from . import views

urlpatterns = [
    path('available/',					views.available,		name='available'),
    path('available/<int:id>',			views.available,		name='available'),
    path('purchased/',			views.purchased,		name='purchased'),
    path('issued/<int:pk>',			views.issued_coupons,		name='issued'),
]