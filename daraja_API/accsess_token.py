import requests
from requests.auth import HTTPBasicAuth
import keys

def my_access_token():
    consumer_key = keys.my_consumer_key
    consumer_secret = keys.my_consumer_secrete

    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

    # print (r.text)
    json_response = r.json()
    access_token = json_response['access_token']
    return access_token
    
