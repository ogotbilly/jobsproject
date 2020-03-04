import requests
from accsess_token import my_access_token
import keys
  
# registering the urls
def register_urls():
    access_token = my_access_token()

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"

    headers = {"Authorization": "Bearer %s" % access_token}

    request = {
        "ShortCode":keys.shotecode,
        "ResponseType": "Completed",
        "ConfirmationURL": "https://d523876e.ngrok.io/home/payments/confirmation",
        "ValidationURL": "https://d523876e.ngrok.io/home/payments/validate",
        }
    try:
      response = requests.post(api_url, json = request, headers=headers)
    except:
      response = requests.post(api_url, json = request, headers=headers, verify=False)

    print (response.text)

# register_urls()

#   end of registering urls

# silulate transaction using B2C 

def simulate_c2b():
    access_token = my_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"

    headers = {"Authorization": "Bearer %s" % access_token}
    request ={ 

                "ShortCode":keys.shotecode,
                "CommandID":"CustomerPayBillOnline",
                "Amount":"1",
                "Msisdn":keys.test_msisdn,
                "BillRefNumber":"33963589" 
                }
    try:

      response = requests.post(api_url, json = request, headers=headers)
    except:
      response = requests.post(api_url, json = request, headers=headers, verify=False)


    print (response.text)

simulate_c2b()
