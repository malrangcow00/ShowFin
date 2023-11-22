from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('save_products/', views.save_products, name='save_products'),
    path('deposit_products/', views.deposit_products, name='deposit_products'),
    path('saving_products/', views.saving_products, name='saving_products'),
    path('deposit_products/<str:fin_prdt_cd>/', views.deposit_options, name='deposit_options'),
    path('saving_products/<str:fin_prdt_cd>/', views.saving_options, name='saving_options'),
    path('deposit_products/top_rate/', views.deposit_top_rate, name='deposit_top_rate'),
    path('saving_products/top_rate/', views.saving_top_rate, name='saving_top_rate'),
    path('get_banks/', views.get_banks, name='get_banks'),
]