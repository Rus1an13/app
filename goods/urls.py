from django.urls import path, URLPattern

from goods import views
app_name = 'goods'

urlpatterns: list[URLPattern] = [
    path('search/', views.catalog, name='search'), # Путь search должен стоять раньше slug, иначе он не будет работать
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
]