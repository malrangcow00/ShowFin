from django.db import models
from django.conf import settings


# Create your models here.
class DepositProducts(models.Model):
    dcls_month = models.TextField()                 # 공시 제출월 [YYYYMM]
    fin_co_no = models.TextField()                  # 금융회사 코드
    fin_prdt_cd = models.TextField(unique=True)     # 금융상품 코드
    kor_co_nm = models.TextField()                  # 금융회사 명
    fin_prdt_nm = models.TextField()                # 금융 상품명
    join_way = models.TextField()                   # 가입 방법
    mtrt_int = models.TextField()                   # 만기 후 이자율
    spcl_cnd = models.TextField()                   # 우대 조건
    join_deny = models.IntegerField()               # 가입제한 Ex) 1:제한없음, 2:서민전용, 3:일부제한
    etc_note = models.TextField()                   # 기타 유의사항
    max_limit = models.IntegerField(null=True)      # 최고한도
    dcls_strt_day = models.TextField()              # 공시 시작일
    dcls_end_day = models.TextField(null=True)      # 공시 종료일
    fin_co_subm_day = models.TextField()            # 금융회사 제출일 [YYYYMMDDHH24MI]

    subscribers = models.ManyToManyField(           # 가입자
        settings.AUTH_USER_MODEL, related_name='subscribed_deposit', blank=True
    )


class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)   # 옵션의 주체 상품
    dcls_month = models.TextField()                 # 공시 제출월 [YYYYMM]
    fin_co_no = models.TextField()                  # 금융회사 코드
    fin_prdt_cd = models.TextField()                # 금융상품 코드
    intr_rate_type = models.TextField()             # 저축 금리 유형
    intr_rate_type_nm = models.TextField()          # 저축 금리 유형명
    save_trm = models.IntegerField()                # 저축 기간 [단위: 개월]
    intr_rate = models.FloatField(null=True)        # 저축 금리 [소수점 2자리]
    intr_rate2 = models.FloatField()                # 최고 우대금리 [소수점 2자리]


class SavingProducts(models.Model):
    dcls_month = models.TextField()                 # 공시 제출월 [YYYYMM]
    fin_co_no = models.TextField()                  # 금융회사 코드
    fin_prdt_cd = models.TextField()                # 금융상품 코드
    kor_co_nm = models.TextField()                  # 금융회사 명
    fin_prdt_nm = models.TextField()                # 금융 상품명
    join_way = models.TextField()                   # 가입 방법
    mtrt_int = models.TextField()                   # 만기 후 이자율
    spcl_cnd = models.TextField()                   # 우대 조건
    join_deny = models.IntegerField()               # 가입제한 Ex) 1:제한없음, 2:서민전용, 3:일부제한
    join_member = models.TextField()                # 가입대상
    etc_note = models.TextField()                   # 기타 유의사항
    min_limit = models.IntegerField(default=0)      # 최저한도
    max_limit = models.IntegerField(null=True)      # 최고한도
    dcls_strt_day = models.TextField()              # 공시 시작일
    dcls_end_day = models.TextField(null=True)      # 공시 종료일
    fin_co_subm_day = models.TextField()            # 금융회사 제출일 [YYYYMMDDHH24MI]

    rsrv_type = models.TextField()                  # 적립 유형 (S : 정액적립식 / F : 자유적립식)

    subscribers = models.ManyToManyField(           # 가입자
        settings.AUTH_USER_MODEL, related_name='subscribed_savings', blank=True
    )


class SavingOptions(models.Model):
    product = models.ForeignKey(SavingProducts, on_delete=models.CASCADE)
    dcls_month = models.TextField()                 # 공시 제출월 [YYYYMM]
    fin_co_no = models.TextField()                  # 금융회사 코드
    fin_prdt_cd = models.TextField()                # 금융상품 코드
    intr_rate_type = models.TextField()             # 저축 금리 유형
    intr_rate_type_nm = models.TextField()          # 저축 금리 유형명

    rsrv_type = models.TextField()                  # 적립 유형 (S : 정액적립식 / F : 자유적립식)
    rsrv_type_nm = models.TextField()               # 적립 유형명

    save_trm = models.IntegerField()                # 저축 기간 [단위: 개월]
    intr_rate = models.FloatField(null=True)        # 저축 금리 [소수점 2자리]
    intr_rate2 = models.FloatField(null=True)       # 최고 우대금리 [소수점 2자리]

class JeonseLoanProducts(models.Model):
    dcls_month = models.TextField()                 # 공시 제출월 [YYYYMM]
    fin_co_no = models.TextField()                  # 금융회사 코드
    fin_prdt_cd = models.TextField()                # 금융상품 코드
    kor_co_nm = models.TextField()                  # 금융회사 명
    fin_prdt_nm = models.TextField()                # 금융 상품명
    join_way = models.TextField()                   # 가입 방법
    loan_inci_expn = models.TextField()             # 대출 부대비용
    erly_rpay_fee = models.TextField()              # 중도상환 수수료
    dly_rate = models.TextField()                   # 연체 이자율
    loan_lmt = models.TextField()                   # 대출한도
    dcls_strt_day = models.TextField()              # 공시 시작일
    dcls_end_day = models.TextField(null=True)      # 공시 종료일
    fin_co_subm_day = models.TextField()            # 금융회사 제출일 [YYYYMMDDHH24MI]

    subscribers = models.ManyToManyField(           # 가입자
        settings.AUTH_USER_MODEL, related_name='subscribed_jeonse_loan', blank=True
    )


class JeonseLoanOptions(models.Model):
    product = models.ForeignKey(JeonseLoanProducts, on_delete=models.CASCADE)
    dcls_month = models.TextField()                 # 공시 제출월 [YYYYMM]
    fin_co_no = models.TextField()                  # 금융회사 코드
    fin_prdt_cd = models.TextField()                # 금융상품 코드
    rpay_type = models.TextField(null=True)         # 대출상환 유형 코드
    rpay_type_nm = models.TextField(null=True)      # 대출 상환유형
    lend_rate_type = models.TextField()             # 대출 금리 유형 코드

    lend_rate_type_nm = models.TextField()          # 대출금리유형
    lend_rate_min = models.FloatField()             # 대출금리 최저[소수점 2자리]
    lend_rate_max = models.FloatField()             # 대출금리 최고[소수점 2자리]
    lend_rate_avg = models.FloatField(null=True)    # 전월 취급 평균금리 [소수점2자리]
