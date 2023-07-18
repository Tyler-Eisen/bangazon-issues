from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from gimmeapi.views.user_view import UserView
from gimmeapi.views.order_view import OrderView
from gimmeapi.views.order_item_view import OrderItemView 
from gimmeapi.views.auth import check_user, register_user
from gimmeapi.views.product_view import ProductView
from gimmeapi.views.category_view import CategoryView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserView, 'user')
router.register(r'orders', OrderView, 'order')
router.register(r'order_items', OrderItemView, 'order_item')
router.register(r'products', ProductView, 'product')
router.register(r'categories', CategoryView, 'category')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('checkuser', check_user),
]
