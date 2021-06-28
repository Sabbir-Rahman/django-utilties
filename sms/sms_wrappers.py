
from twilio.rest import Client
import environ

def send_sms_twilio(phone_no):
    env = environ.Env()
    environ.Env.read_env()
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid =  env('TWILIO_ACCOUNT_SID')
    auth_token = env('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="This is testing from twilio in django utility",
                        from_='+19708250719',
                        to= phone_no
                    )

    print(message.sid)
    return phone_no