from rest_framework import serializers
from .models import Deal, Product
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "articul", "price", "preview", "count_product")


class DealSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True, required=False)

    class Meta:
        model = Deal
        fields = ("id", "product", "user_count_product")


class UserSerializer(serializers.ModelSerializer):
    deal = DealSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password", "deal")
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
            )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
