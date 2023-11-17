from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('save_products/', views.save_products, name='save_products'),
    path('deposit_products/', views.deposit_products, name='deposit_products'),
    path('savings_products/', views.savings_products, name='savings_products'),
    path('deposit_product_options/<str:fin_prdt_cd>/', views.deposit_product_options, name='deposit_product_options'),
    path('savings_product_options/<str:fin_prdt_cd>/', views.savings_product_options, name='savings_product_options'),
    path('deposit_products/top_rate/', views.deposit_top_rate, name='deposit_top_rate'),
    path('savings_products/top_rate/', views.savings_top_rate, name='savings_top_rate'),
    path('get_banks/', views.get_banks, name='get_banks'),
]
