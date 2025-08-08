from rest_framework import serializers
from .models import CustomUser
from django.core.validators import ValidationError
from rest_framework import status

class RegisterSerilizers(serializers.ModelSerializer):
    password = serializers.CharField(max_length=15)
    confirm_password = serializers.CharField(max_length=15)
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username','age','address','password','confirm_password']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise ValidationError({'message':'Parollar mos emas!','status':status.HTTP_400_BAD_REQUEST})
        username = data['username']
        if CustomUser.objects.filter(username = username).exists():
            raise ValidationError({'message': 'Bu username ruyxatdan utgan!', 'status': status.HTTP_400_BAD_REQUEST})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = CustomUser.objects.create(
            username = validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            age=validated_data['age'],
            address=validated_data['address'],
        )
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user = user)
        return user