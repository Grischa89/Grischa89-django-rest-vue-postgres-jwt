from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
# from .serializers import UserSerializerWithToken


from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class UserActivationView(APIView):
    def get (self, request, uid, token):
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + "/api/v1/accounts/users/activate/"
        post_data = {'uid': uid, 'token': token}
        result = requests.post(post_url, data = post_data)
        content = result.text
        print("reuslt:", result)
        print("content:", content)
        return Response(content)

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