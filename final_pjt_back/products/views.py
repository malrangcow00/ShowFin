# from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from .models import DepositProducts, DepositOptions, SavingProducts, SavingOptions, JeonseLoanProducts, JeonseLoanOptions
from .serializers import DepositProductsSerializer, DepositOptionsSerializer, SavingProductsSerializer, SavingOptionsSerializer, JeonseLoanProductsSerializer, JeonseLoanOptionsSerializer, DepositSerializer, SavingSerializer, JeonseLoanSerializer, SubscribeSerializer

# Create your views here.


API_KEY = settings.API_KEY
BASE_URL = settings.BASE_URL
DEPOSIT = settings.DEPOSIT
SAVING = settings.SAVING
LOAN = settings.LOAN
COMPANY = settings.COMPANY
BANK_TYPE = settings.BANK_TYPE
LOAN_TYPE = settings.LOAN_TYPE
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

    for product in response.get('result').get('baseList'):
        # 중복체크
        if DepositProducts.objects.filter(fin_prdt_cd=product.get('fin_prdt_cd')).exists():
            continue

        save_data = {
            'dcls_month' : product.get('dcls_month'),
            'fin_co_no' : product.get('fin_co_no'),
            'fin_prdt_cd' : product.get('fin_prdt_cd'),
            'kor_co_nm' : product.get('kor_co_nm'),
            'fin_prdt_nm' : product.get('fin_prdt_nm'),
            'join_way' : product.get('join_way'),
            'mtrt_int' : product.get('mtrt_int'),
            'spcl_cnd' : product.get('spcl_cnd'),
            'join_deny' : product.get('join_deny'),
            'etc_note' : product.get('etc_note'),
            'max_limit' : product.get('max_limit'),
            'dcls_strt_day' : product.get('dcls_strt_day'),
            'dcls_end_day' : product.get('dcls_end_day'),
            'fin_co_subm_day' : product.get('fin_co_subm_day'),
        }
        serializer = DepositProductsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        # 옵션 목록 저장
    for option in response.get('result').get('optionList'):
        # 중복체크
        if DepositOptions.objects.filter(fin_prdt_cd=option.get('fin_prdt_cd'), save_trm=option.get('save_trm')).exists():
            continue

        save_data = {
            'dcls_month' : option.get('dcls_month'),
            'fin_co_no' : option.get('fin_co_no'),
            'fin_prdt_cd' : option.get('fin_prdt_cd'),
            'intr_rate_type' : option.get('intr_rate_type'),
            'intr_rate_type_nm' : option.get('intr_rate_type_nm'),
            'save_trm' : option.get('save_trm'),
            'intr_rate' : option.get('intr_rate'),
            'intr_rate2' : option.get('intr_rate2'),
        }
        serializer = DepositOptionsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            product = DepositProducts.objects.get(fin_prdt_cd=option.get('fin_prdt_cd'))
            serializer.save(product=product)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # 적금 상품 저장 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    URL = BASE_URL + SAVING
    response = requests.get(URL, params=params).json()

    for product in response.get('result').get('baseList'):
        # 1. 자유적립, 정액적립 상품 저장
        for rsrv_type in ['S', 'F']:
            # 중복체크
            if SavingProducts.objects.filter(fin_prdt_cd=product.get('fin_prdt_cd'), rsrv_type=rsrv_type).exists():
                continue

            save_data = {
                'dcls_month' : product.get('dcls_month'),
                'fin_co_no' : product.get('fin_co_no'),
                'fin_prdt_cd' : product.get('fin_prdt_cd'),
                'kor_co_nm' : product.get('kor_co_nm'),
                'fin_prdt_nm' : product.get('fin_prdt_nm'),
                'join_way' : product.get('join_way'),
                'mtrt_int' : product.get('mtrt_int'),
                'spcl_cnd' : product.get('spcl_cnd'),
                'join_deny' : product.get('join_deny'),
                'join_member' : product.get('join_member'),
                'etc_note' : product.get('etc_note'),
                'max_limit' : product.get('max_limit'),
                'dcls_strt_day' : product.get('dcls_strt_day'),
                'dcls_end_day' : product.get('dcls_end_day'),
                'fin_co_subm_day' : product.get('fin_co_subm_day'),
                'rsrv_type' : rsrv_type,
            }
            serializer = SavingProductsSerializer(data=save_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

    for option in response.get('result').get('optionList'):
        # 중복 체크
        if SavingOptions.objects.filter(fin_prdt_cd=option.get('fin_prdt_cd'), rsrv_type=option.get('rsrv_type'), save_trm=option.get('save_trm')).exists():
            continue

        save_data = {
            'dcls_month' : option.get('dcls_month'),
            'fin_co_no' : option.get('fin_co_no'),
            'fin_prdt_cd' : option.get('fin_prdt_cd'),
            'intr_rate_type' : option.get('intr_rate_type'),
            'intr_rate_type_nm' : option.get('intr_rate_type_nm'),

            'rsrv_type' : option.get('rsrv_type'),
            'rsrv_type_nm' : option.get('rsrv_type_nm'),

            'save_trm' : option.get('save_trm'),
            'intr_rate' : option.get('intr_rate'),
            'intr_rate2' : option.get('intr_rate2'),
        }
        serializer = SavingOptionsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            product = SavingProducts.objects.get(fin_prdt_cd=option.get('fin_prdt_cd'), rsrv_type=option.get('rsrv_type'))
            serializer.save(product=product)

    # 2. 옵션이 없는 상품 삭제
    products = SavingProducts.objects.all()
    for product in products:
        if len(product.savingoptions_set.all()) == 0:
            product.delete()
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # 전세 대출 상품 저장 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    URL = BASE_URL + LOAN
    # MAX_PAGE_NO = 6
    for number in range(1, 6):
        params = {
            'auth' : API_KEY,
            'topFinGrpNo' : LOAN_TYPE,
            'pageNo' : number,
        }

        response = requests.get(URL, params=params).json()

        for product in response.get('result').get('baseList'):
            # 중복 체크
            if JeonseLoanProducts.objects.filter(fin_prdt_cd=product.get('fin_prdt_cd'), fin_co_no=product.get('fin_co_no')).exists():
                    continue
            
            save_data = {
                'dcls_month' : product.get('dcls_month'),       
                'fin_co_no' : product.get('fin_co_no'),
                'fin_prdt_cd' : product.get('fin_prdt_cd'),
                'kor_co_nm' : product.get('kor_co_nm'),
                'fin_prdt_nm' : product.get('fin_prdt_nm'),
                'join_way' : product.get('join_way'),
                
                'loan_inci_expn' : product.get('loan_inci_expn'),
                'erly_rpay_fee' : product.get('erly_rpay_fee'),
                'dly_rate' : product.get('dly_rate'),
                'join_member' : product.get('join_member'),
                
                'loan_lmt' : product.get('loan_lmt'),
                'dcls_strt_day' : product.get('dcls_strt_day'),
                'dcls_end_day' : product.get('dcls_end_day'),
                'fin_co_subm_day' : product.get('fin_co_subm_day'),
            }
            serializer = JeonseLoanProductsSerializer(data=save_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

        for option in response.get('result').get('optionList'):
            # 이미 있는 데이터면 통과
            if JeonseLoanOptions.objects.filter(
                fin_co_no=option.get('fin_co_no'),
                fin_prdt_cd=option.get('fin_prdt_cd'),
                rpay_type=option.get('rpay_type'),
                lend_rate_type=option.get('lend_rate_type')
                ).exists():
                continue

            save_data = {
                'dcls_month' : option.get('dcls_month'),
                'fin_co_no' : option.get('fin_co_no'),
                'fin_prdt_cd' : option.get('fin_prdt_cd'),
                'rpay_type' : option.get('rpay_type'),
                'rpay_type_nm' : option.get('rpay_type_nm'),
                'lend_rate_type' : option.get('lend_rate_type'),

                'lend_rate_type_nm' : option.get('lend_rate_type_nm'),
                'lend_rate_min' : option.get('lend_rate_min'),
                'lend_rate_max' : option.get('lend_rate_max'),
                'lend_rate_avg' : option.get('lend_rate_avg'),
            }
            serializer = JeonseLoanOptionsSerializer(data=save_data)
            if serializer.is_valid(raise_exception=True):
                product = JeonseLoanProducts.objects.get(fin_prdt_cd=option.get('fin_prdt_cd'), fin_co_no=option.get('fin_co_no'))
                serializer.save(product=product)

    # 저장완료 메세지
    # return JsonResponse({ 'message' : 'GOOD'})

    return Response({ 'message' : 'OKAY'})

@api_view(['GET'])
def deposits(request):
    products = DepositProducts.objects.all()
    serializer = DepositSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def savings(request):
    products = SavingProducts.objects.all()
    serializer = SavingSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def loans(request):
    products = JeonseLoanProducts.objects.all()
    serializer = JeonseLoanSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
def subscribe_info(request):
    if request.method == 'GET':
        serializer = SubscribeSerializer(request.user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SubscribeSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        
@api_view(['POST'])
def subscribe(request, prdt_type, product_pk):
    if prdt_type == 'deposit':
        product = DepositProducts.objects.get(pk=product_pk)
        if product.subscribers.filter(pk=request.user.pk).exists():
            product.subscribers.remove(request.user)
            return Response({ 'message': 'Successfully unsubscribed!' })
        else:
            product.subscribers.add(request.user)
            return Response({ 'message': 'Successfully subscribed!' })
        
    elif prdt_type == 'savings':
        product = SavingProducts.objects.get(pk=product_pk)
        if product.subscribers.filter(pk=request.user.pk).exists():
            product.subscribers.remove(request.user)
            return Response({ 'message': 'Successfully unsubscribed!' })
        else:
            product.subscribers.add(request.user)
            return Response({ 'message': 'Successfully subscribed!' })
    
    elif prdt_type == 'jeonse':
        product = JeonseLoanProducts.objects.get(pk=product_pk)
        if product.subscribers.filter(pk=request.user.pk).exists():
            product.subscribers.remove(request.user)
            return Response({ 'message': 'Successfully unsubscribed!' })
        else:
            product.subscribers.add(request.user)
            return Response({ 'message': 'Successfully subscribed!' })



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# @api_view(['GET', 'POST'])
# def deposit_products(request):
#     if request.method == 'GET':
#         products = DepositProducts.objects.all()
#         serializer = DepositProductsSerializer(products, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = DepositProductsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         data = {
#             'message': f'이미 있는 데이터이거나, 데이터가 잘못 입력되었습니다.',
#         }
#         return Response(data, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])
# def savings_products(request):
#     if request.method == 'GET':
#         products = SavingProducts.objects.all()
#         serializer = SavingProductsSerializer(products, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = SavingProductsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         data = {
#             'message': f'이미 있는 데이터이거나, 데이터가 잘못 입력되었습니다.',
#         }
#         return Response(data, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def deposit_product_options(request, fin_prdt_cd):
#     options = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
#     serializer = DepositOptionsSerializer(options, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def savings_product_options(request, fin_prdt_cd):
#     options = SavingOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
#     serializer = SavingOptionsSerializer(options, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def deposit_top_rate(request):
#     rate = 0
#     options = DepositOptions.objects.all()
#     for option in options:
#         if option.intr_rate2 >= rate:
#             rate = option.intr_rate2

#     filter_options = DepositOptions.objects.filter(intr_rate2=rate)
#     # print(filter_options)
#     data = {
#         "deposit_product": [],
#         "options": []
#     }
#     for filter_option in filter_options:
#         filter_product = filter_option.product

#         product_serializer = DepositProductsSerializer(filter_product)
#         option_serializer = DepositOptionsSerializer(filter_option)

#         data["deposit_product"].append(product_serializer.data)
#         data["options"].append(option_serializer.data)

#     return Response(data)



# @api_view(['GET'])
# def savings_top_rate(request):
#     rate = 0
#     options = SavingOptions.objects.all()
#     for option in options:
#         if option.intr_rate2 >= rate:
#             rate = option.intr_rate2

#     filter_options = SavingOptions.objects.filter(intr_rate2=rate)
#     # print(filter_options)
#     data = {
#         "savings_product": [],
#         "options": []
#     }
#     for filter_option in filter_options:
#         filter_product = filter_option.product

#         product_serializer = SavingProductsSerializer(filter_product)
#         option_serializer = SavingOptionsSerializer(filter_option)

#         data["savings_product"].append(product_serializer.data)
#         data["options"].append(option_serializer.data)

#     return Response(data)

# @api_view(['GET', 'POST'])
# def savings_products(request):
#     if request.method == 'GET':
#         products = SavingProducts.objects.all()
#         serializer = SavingProductsSerializer(products, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = SavingProductsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         data = {
#             'message': f'이미 있는 데이터이거나, 데이터가 잘못 입력되었습니다.',
#         }
#         return Response(data, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def deposit_product_options(request, fin_prdt_cd):
#     options = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
#     serializer = DepositOptionsSerializer(options, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def savings_product_options(request, fin_prdt_cd):
#     options = SavingOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
#     serializer = SavingOptionsSerializer(options, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def deposit_top_rate(request):
#     rate = 0
#     options = DepositOptions.objects.all()
#     for option in options:
#         if option.intr_rate2 >= rate:
#             rate = option.intr_rate2

#     filter_options = DepositOptions.objects.filter(intr_rate2=rate)
#     # print(filter_options)
#     data = {
#         "deposit_product": [],
#         "options": []
#     }
#     for filter_option in filter_options:
#         filter_product = filter_option.product

#         product_serializer = DepositProductsSerializer(filter_product)
#         option_serializer = DepositOptionsSerializer(filter_option)

#         data["deposit_product"].append(product_serializer.data)
#         data["options"].append(option_serializer.data)

#     return Response(data)



# @api_view(['GET'])
# def savings_top_rate(request):
#     rate = 0
#     options = SavingOptions.objects.all()
#     for option in options:
#         if option.intr_rate2 >= rate:
#             rate = option.intr_rate2

#     filter_options = SavingOptions.objects.filter(intr_rate2=rate)
#     # print(filter_options)
#     data = {
#         "savings_product": [],
#         "options": []
#     }
#     for filter_option in filter_options:
#         filter_product = filter_option.product

#         product_serializer = SavingProductsSerializer(filter_product)
#         option_serializer = SavingOptionsSerializer(filter_option)

#         data["savings_product"].append(product_serializer.data)
#         data["options"].append(option_serializer.data)

#     return Response(data)


@api_view(['GET'])
def get_banks(request):
    URL = BASE_URL + COMPANY
    params = {
        'auth': API_KEY,
        'topFinGrpNo': BANK_TYPE,
        'pageNo': PAGE_NO,
    }

    # response = requests.get(URL, params=params).encoding = 'utf-8'
    response = requests.get(URL, params=params).json()
    # response = response.json()

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
    print(JsonResponse(data))
    return JsonResponse(data)
