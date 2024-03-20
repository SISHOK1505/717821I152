from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_company, name='register_company'),
    path('auth/', views.obtain_auth_token, name='obtain_auth_token'),
    path('<str:company_name>/<str:category_name>/', views.get_top_products, name='get_top_products'),
]
