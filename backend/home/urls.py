from django.urls import path
from .views import CartGenericAPIView
urlpatterns = [
    path("cart/",CartGenericAPIView.as_view(),name="cart_list_create")
]