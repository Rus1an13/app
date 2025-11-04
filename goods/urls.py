from django.urls import path, URLPattern

from goods import views
app_name = 'goods'

urlpatterns: list[URLPattern] = [
    path('', views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
]