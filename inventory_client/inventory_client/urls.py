from django.contrib import admin
from django.urls import path
from inventory_client_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('product-detail/', views.product_detail, name='product_detail'),
]
