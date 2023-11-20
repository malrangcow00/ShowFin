# from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from .models import DepositProducts, DepositOptions, SavingProducts, SavingOptions
from .serializers import DepositProductsSerializer, DepositOptionsSerializer, SavingProductsSerializer, SavingOptionsSerializer

# Create your views here.

# def save_db(response, type):
#     # 상품 목록 저장
#     # deposit_products = response.get("result").get("baseList")
#     # deposit_products_serializer = DepositProductsSerializer(data=deposit_products, many=True)
#     # if deposit_products_serializer.is_valid(raise_exception=True):
#     #     deposit_products_serializer.save()
#     for product_type in response.get("result").get("baseList"):
#         # print(product_type)

#         save_data = {
#             'fin_prdt_cd': product_type.get('fin_prdt_cd'),
#             'kor_co_nm': product_type.get('kor_co_nm'),
#             'fin_prdt_nm': product_type.get('fin_prdt_nm'),
#             'etc_note': product_type.get('etc_note'),
#             'join_deny': product_type.get('join_deny'),
#             'join_member': product_type.get('join_member'),
#             'join_way': product_type.get('join_way'),
#             'spcl_cnd': product_type.get('spcl_cnd'),
#         }
    
#         # 저장하기 위해 데이터를 포장
#         serializer = type[2](data=save_data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()


#     # 옵션 목록 저장
#     for option in response.get("result").get("optionList"):
#         # print(deposit)
#         save_data = {
#             'fin_prdt_cd': option.get('fin_prdt_cd'),
#             'intr_rate_type_nm': option.get('intr_rate_type_nm'),
#             'intr_rate': option.get('intr_rate'),
#             'intr_rate2': option.get('intr_rate2'),
#             'save_trm': option.get('save_trm'),
#         }
    
#         # 저장하기 위해 데이터를 포장
#         product = type[1].objects.get(fin_prdt_cd=save_data.get('fin_prdt_cd'))
#         serializer = type[3](data=save_data, partial=True)
        
#         for key in save_data:
#             if not save_data[key]:
#                 save_data[key] = -1

#         if serializer.is_valid(raise_exception=True):
#             #product
#             serializer.save(product=product)


API_KEY = settings.API_KEY
BASE_URL = settings.BASE_URL
DEPOSIT = settings.DEPOSIT
SAVINGS = settings.SAVINGS
COMPANY = settings.COMPANY
BANK_TYPE = settings.BANK_TYPE
PAGE_NO = settings.PAGE_NO


@api_view(['GET'])
def save_products(request):
    params = {
        'auth' : API_KEY,
        'topFinGrpNo' : BANK_TYPE,
        'pageNo' : PAGE_NO,
    }

    # 예금 상품 저장 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    URL = BASE_URL + DEPOSIT
    response = requests.get(URL, params=params).json()

    deposit_products = response.get("result").get("baseList")
    deposit_products_serializer = DepositProductsSerializer(data=deposit_products, many=True)
    if deposit_products_serializer.is_valid(raise_exception=True):
        deposit_products_serializer.save()

        # 옵션 목록 저장
    for option in response.get("result").get("optionList"):
        save_data = {
            'fin_prdt_cd': option.get('fin_prdt_cd'),
            'intr_rate_type_nm': option.get('intr_rate_type_nm'),
            'intr_rate': option.get('intr_rate'),
            'intr_rate2': option.get('intr_rate2'),
            'save_trm': option.get('save_trm'),
        }
    
        # 저장하기 위해 데이터를 포장
        product = DepositProducts.objects.get(fin_prdt_cd=save_data.get('fin_prdt_cd'))
        serializer = DepositOptionsSerializer(data=save_data, partial=True)
        
        for key in save_data:
            if not save_data[key]:
                save_data[key] = -1

        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)
    
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # 적금 상품 저장 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    URL = BASE_URL + SAVINGS
    response = requests.get(URL, params=params).json()

    savings_products = response.get("result").get("baseList")
    savings_products_serializer = SavingProductsSerializer(data=savings_products, many=True)
    if savings_products_serializer.is_valid(raise_exception=True):
        savings_products_serializer.save()

    for option in response.get("result").get("optionList"):
        save_data = {
            'fin_prdt_cd': option.get('fin_prdt_cd'),
            'intr_rate_type_nm': option.get('intr_rate_type_nm'),
            'intr_rate': option.get('intr_rate'),
            'intr_rate2': option.get('intr_rate2'),
            'save_trm': option.get('save_trm'),
        }
    
        # 저장하기 위해 데이터를 포장
        product = SavingProducts.objects.get(fin_prdt_cd=save_data.get('fin_prdt_cd'))
        serializer = SavingOptionsSerializer(data=save_data, partial=True)
        
        for key in save_data:
            if not save_data[key]:
                save_data[key] = -1

        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # 저장완료 메세지
    # return JsonResponse({ 'message' : 'GOOD'})
    return Response({ 'message' : 'OKAY'})


@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'GET':
        products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        data = {
            'message': f'이미 있는 데이터이거나, 데이터가 잘못 입력되었습니다.',
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def savings_products(request):
    if request.method == 'GET':
        products = SavingProducts.objects.all()
        serializer = SavingProductsSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SavingProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        data = {
            'message': f'이미 있는 데이터이거나, 데이터가 잘못 입력되었습니다.',
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    options = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(options, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def savings_product_options(request, fin_prdt_cd):
    options = SavingOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = SavingOptionsSerializer(options, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def deposit_top_rate(request):
    rate = 0
    options = DepositOptions.objects.all()
    for option in options:
        if option.intr_rate2 >= rate:
            rate = option.intr_rate2

    filter_options = DepositOptions.objects.filter(intr_rate2=rate)
    # print(filter_options)
    data = {
        "deposit_product": [],
        "options": []
    }
    for filter_option in filter_options:
        filter_product = filter_option.product

        product_serializer = DepositProductsSerializer(filter_product)
        option_serializer = DepositOptionsSerializer(filter_option)
        
        data["deposit_product"].append(product_serializer.data)
        data["options"].append(option_serializer.data)
    
    return Response(data)



@api_view(['GET'])
def savings_top_rate(request):
    rate = 0
    options = SavingOptions.objects.all()
    for option in options:
        if option.intr_rate2 >= rate:
            rate = option.intr_rate2

    filter_options = SavingOptions.objects.filter(intr_rate2=rate)
    # print(filter_options)
    data = {
        "savings_product": [],
        "options": []
    }
    for filter_option in filter_options:
        filter_product = filter_option.product

        product_serializer = SavingProductsSerializer(filter_product)
        option_serializer = SavingOptionsSerializer(filter_option)
        
        data["savings_product"].append(product_serializer.data)
        data["options"].append(option_serializer.data)
    
    return Response(data)


@api_view(['GET'])
def get_banks(request):
    URL = BASE_URL + COMPANY
    params = {
        'auth' : API_KEY,
        'topFinGrpNo' : BANK_TYPE,
        'pageNo' : PAGE_NO,
    }

    response = requests.get(URL, params=params).encoding = 'utf-8'
    response = response.json()

    data = {
        'company_name': [],
    }

    for company_info in response.get("result").get("baseList"):
        company_name = company_info.get('kor_co_nm')
        if company_name in data['company_name']:
            continue
        data['company_name'].append(company_name)

    print(JsonResponse(data))
    return JsonResponse(data)