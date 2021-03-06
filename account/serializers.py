from rest_framework  import serializers
from .models import Register, Login


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ('id', 'first_name', 'last_name', 'username', 'password')


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('id', 'username', 'password')
