from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='products'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('signup/', views.signup, name='signup'),
    path('user/', views.user_page, name='user'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]