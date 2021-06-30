from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .email_wrappers import Util
from django.http import response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from rest_framework import generics, serializers,status
from .serializers import userSerializer
# Create your views here.

# http://127.0.0.1:8000/sms/send/
@api_view(['POST'])
def send_email(request):
    

    email = request.POST['email']

    user_obj = User.objects.create(email=email)

    #sending token for email verification
    token = RefreshToken.for_user(user=user_obj).access_token

    current_site = get_current_site(request).domain

    relative_link = reverse('email-verify')

    absurl = 'http://'+current_site+relative_link+"?token="+str(token)

    email_body = 'Hi '+ '. Use link below to verify your email \n \n'+absurl
    data ={'to_email':email,'email_body':email_body,'email_subject': 'Verify your email'}

    Util.send_email(data)
    
   

    res = {
        'message': 'Email send to '+ str(email),
    }
    return Response(res, status=200)


#verify email 
@api_view(['GET'])
def verify_email(request):
    token = request.GET.get('token')
  
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        user = User.objects.get(id=payload['user_id'])
        

        if not user.verified:
            user.verified = True
            user.save()

        return Response({'email':'Succesfully verified go back to login page for login'},status=status.HTTP_200_OK)

    except jwt.ExpiredSignatureError as identifier:
       return Response({'email':'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
    except jwt.exceptions.DecodeError as identifier:
        return Response({'email':'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)



#verify email 
@api_view(['GET'])
def view_user(request):
    user = User.objects.all()
    serializer = userSerializer(user, many= True)
    return Response(serializer.data)
