from rest_framework import serializers
from .models import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['name','email','age']

    # validation of age must b/w 0 and 120
    def validate_age(self,age_value):
        if age_value < 0 or age_value > 120:
            raise serializers.ValidationError("age must b/w 0 and 120.")
        return age_value