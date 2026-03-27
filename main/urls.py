from django.urls import path, URLPattern

from main import views
app_name = 'main' # Обязательно нужно задать имя приложения

urlpatterns: list[URLPattern] = [
    path('', views.IndexView.as_view(), name='index'),
    path('about', views.AboutView.as_view(), name='about'),
]