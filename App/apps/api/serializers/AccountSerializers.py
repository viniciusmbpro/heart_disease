from rest_framework import serializers

from apps.account.models import Account


class AccountBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id', 'email', 'username',
            'first_name', 'last_name', 'password',
        ]


class AccountAnonymousSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id', 'email', 'username', 'first_name',
        ]


class AccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id', 'email',
            'username', 'first_name', 'last_name',
            'created_at', 'modified_at', 'last_login',
            'photo'
        ]
