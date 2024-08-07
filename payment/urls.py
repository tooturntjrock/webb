from django.urls import path, include
from . import views

app_name = 'payment'

urlpatterns = [
    path('payment_success/', views.payment_success, name="payment_success"),
    path('checkout/', views.checkout, name="checkout"),
    path('billing_info/', views.billing_info, name="billing_info"),
    path('process_order/', views.process_order, name="process_order"),
    path('shipped_items/', views.shipped_items, name="shipped_items"),
    path('not_shipped_items/', views.not_shipped_items, name="not_shipped_items"),
    path('orders/<int:pk>', views.orders, name="orders"),
    path('paypal/', include("paypal.standard.ipn.urls")),
    path('payment_failed/', views.payment_failed, name="payment_failed")
    
    
]