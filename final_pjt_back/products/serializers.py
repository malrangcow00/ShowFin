from rest_framework import serializers
from .models import DepositProducts, DepositOptions, SavingProducts, SavingOptions, JeonseLoanProducts, JeonseLoanOptions
from django.contrib.auth import get_user_model

# 예금
class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'


class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        exclude = ('product', )
        read_only_fields = ('product', )


class DepositSerializer(serializers.ModelSerializer):
    depositoptions_set = DepositOptionsSerializer(many=True, read_only=True)

    class Meta:
        model = DepositProducts
        fields = '__all__'


# 적금
class SavingProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'


class SavingOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        exclude = ('product', )
        read_only_fields = ('product', )


class SavingSerializer(serializers.ModelSerializer):
    savingoptions_set = SavingOptionsSerializer(many=True, read_only=True)

    class Meta:
        model = SavingProducts
        fields = '__all__'


# 전세자금대출
class JeonseLoanProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JeonseLoanProducts
        fields = '__all__'


class JeonseLoanOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JeonseLoanOptions
        exclude = ('product',)
        read_only_fields = ('product',)
        

class JeonseLoanSerializer(serializers.ModelSerializer):
    jeonseloanoptions_set = JeonseLoanOptionsSerializer(many=True, read_only=True)

    class Meta:
        model = JeonseLoanProducts
        fields = '__all__'
        

class SubscribeSerializer(serializers.ModelSerializer):
    subscribed_deposits = DepositSerializer(many=True, read_only=True)
    subscribed_savings = SavingSerializer(many=True, read_only=True)
    subscribed_jeonse_loan = JeonseLoanSerializer(many=True, read_only=True)
    
    class Meta:
        model = get_user_model()
        fields = '__all__'