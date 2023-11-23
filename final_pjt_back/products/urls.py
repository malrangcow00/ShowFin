from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('save_products/', views.save_products, name='save_products'),                      # 상품 저장
    path('deposits/', views.deposits, name='deposits'),                                     # 예금 상품 리스트 조회
    path('savings/', views.savings, name='savings'),                                        # 적금 상품 리스트 조회
    path('loans/', views.loans, name='loans'),                                           # 전세자금대출 상품 리스트 조회
    path('subscribe/<str:prdt_type>/<int:product_id>/', views.subscribe, name='subscribe'),  # 상품 구독
    path('get_banks/', views.get_banks, name='get_banks'),                                  # 은행 리스트 조회
]
