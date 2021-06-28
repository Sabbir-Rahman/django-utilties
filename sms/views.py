from django.http import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .sms_wrappers import send_sms_twilio


# Create your views here.
# http://127.0.0.1:8000/sms/send/
@api_view(['POST'])
def send_sms(request):
    

    phone_no = request.POST['phone_no']

    response_sms = send_sms_twilio(phone_no)
    # Get environment variables
    USER = 'sfdfsdfds'
   

    res = {
        'response_sms' : response_sms,
        'message': 'Sms send to '+ str(phone_no)
    }
    return Response(res, status=200)
