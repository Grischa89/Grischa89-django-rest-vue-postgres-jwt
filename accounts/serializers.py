from rest_framework import serializers
from django.contrib.auth.models import User
# from rest_framework_simplejwt.tokens import RefreshToken


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
                validated_data['username'],
                validated_data['email'],
                validated_data['password'])
        user.save()
        user_profile = UserProfile(user=user)
        user_profile.save()
        return user_profile

# class UserSerializerWithToken(UserSerializer):
#     token = serializers.SerializerMethodField(read_only=True)
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email']
