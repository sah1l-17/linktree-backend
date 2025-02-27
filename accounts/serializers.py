from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser, Referral, Reward

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'referral_code', 'referred_by')

    def create(self, validated_data):
        password = validated_data.pop('password')
        referred_by = validated_data.pop('referred_by', None)

        user = User(**validated_data)
        user.set_password(password)
        user.save()

        if referred_by:
            referrer = User.objects.filter(referral_code=referred_by).first()
            if referrer:
                Referral.objects.create(referrer=referrer, referred_user=user, status="successful")
                reward, created = Reward.objects.get_or_create(user=referrer)
                reward.add_points(10)

        return user
