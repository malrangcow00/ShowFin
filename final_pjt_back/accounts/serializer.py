from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer,UserDetailsSerializer
# from django.conf import settings
from django.contrib.auth import get_user_model


# 커스텀 회원가입 시리얼라이저
class CustomRegisterSerializer(RegisterSerializer):
    # 추가할 필드들을 정의합니다.
    # username = serializers.CharField(max_length=30)
    nickname = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255
    )
    # email = serializers.EmailField(required=False)
    age = serializers.IntegerField(required=False)
    wealth = serializers.IntegerField(required=False)
    salary = serializers.IntegerField(required=False)
    financial_products = serializers.ListField(child=serializers.IntegerField(), required=False)
    # is_active = serializers.BooleanField(default=True)
    # is_staff = serializers.BooleanField(default=False)
    # is_superuser = serializers.BooleanField(default=False)

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'age': self.validated_data.get('age', ''),
            'wealth': self.validated_data.get('wealth', ''),
            'salary': self.validated_data.get('salary', ''),
            'financial_products': self.validated_data.get('financial_products', ''),
        }
    
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user


# 커스텀 로그인 시리얼라이저
class CustomLoginSerializer(LoginSerializer):
    # email 필드 제거
    email = None


# 유저 시리얼라이저
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('pk','username', 'nickname', 'email', 'age', 'wealth', 'salary', 'financial_products', )


# 유저 디테일 시리얼라이저
class CustomUserDetailsSerializer(UserDetailsSerializer):
    age = serializers.IntegerField(required=False)
    nickname = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255
    )
    salary = serializers.IntegerField(required=False)
    wealth = serializers.IntegerField(required=False)
    financial_products = serializers.ListField(child=serializers.IntegerField(), required=False)
    
    class Meta(UserDetailsSerializer.Meta):
        # 기본적으로 pk, username, email, first_name, last_name 출력함
        fields = UserDetailsSerializer.Meta.fields + ('age', 'nickname', 'salary', 'wealth', 'financial_products')
        read_only_fields = ('username', )


    def get_cleaned_data(self):
        data_obj = {}
        # data_obj = super().get_cleaned_data()
        # data_obj['username'] = self.validated_data.get('username', '')
        data_obj['age'] = self.validated_data.get('age', '')
        data_obj['nickname'] = self.validated_data.get('nickname', '')
        data_obj['salary'] = self.validated_data.get('salary', '')
        data_obj['wealth'] = self.validated_data.get('wealth', '')
        data_obj['financial_products'] = self.validated_data.get('financial_products', '')
        return data_obj
    

    def update(self, instance, validated_data): 
        instance = super().update(instance, validated_data)
        # instance.username = validated_data.get('username', '')
        instance.age = validated_data.get('age', '')
        instance.nickname = validated_data.get('nickname', '')
        instance.salary = validated_data.get('salary', '')
        instance.wealth = validated_data.get('wealth', '')
        instance.financial_products = validated_data.get('financial_products', '')
        instance.save()
        return instance
    

    def save(self):
        # self.validated_data.pop('username', None)
        user = super().save()
        user.age = self.validated_data.get('age', '')
        user.nickname = self.validated_data.get('nickname', '')
        user.salary = self.validated_data.get('salary', '')
        user.wealth = self.validated_data.get('wealth', '')
        user.financial_products = self.validated_data.get('financial_products', '')
        user.save()
        return user
