from django.db import models


# Create your models here.
class DepositProduct(models.Model):
    fin_prdt_cd = models.TextField()
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()

    def __str__(self):
        return self.fin_prdt_nm


class DepositOption(models.Model):
    product_pk = models.ForeignKey(DepositProduct, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.TextField()
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()


class SavingProduct(models.Model):
    fin_prdt_cd = models.TextField()
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()

    def __str__(self):
        return self.fin_prdt_nm


class SavingOption(models.Model):
    product_pk = models.ForeignKey(SavingProduct, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.TextField()
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()
