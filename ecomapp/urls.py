from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home, name="Home"),
    path('cart/', views.CartPage, name="cart"),
    path('AddtoCart/<int:product_id>/' , views.AddtoCart, name="AddtoCart"),
    path('DeleteCartItem/<int:product_id>/', views.DeleteCartItem, name="DeleteCartItem")
]