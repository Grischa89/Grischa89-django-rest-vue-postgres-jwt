from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
# from .serializers import UserSerializerWithToken

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):


    # def get_token(cls, user):
    #     return RefreshToken.for_user(user)
    def get_token(cls, user):
        token = super().get_token(user)
        print("type: ", type(token))
        token['access'] = "mad"
        token['username'] = user.username
        token['email'] = user.email
        token['is_staff'] = user.is_staff
        token['penis'] = "penis"
        return token

    def validate(self, attrs):
        if attrs:
            print("attrs", attrs, )

        data = super().validate(attrs)
        print(dir(self.user))
        data['username'] = self.user.username
        data['email'] = self.user.email
        data['is_staff'] = self.user.is_staff
        
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer