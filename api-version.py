import requests
import json

def prodUrl(apiName):
    return 'https://api.burberry.com/services/' +apiName + '/v1/health-check'

def preprodUrl(apiName):
    return 'https://preprod-api.apps.burberry.com/services/' +apiName + '/v1/health-check'

apiList = [  'sites',
  'customers',
  'carts',
  'gift-cards',
  'inventory',
  'orders',
  'favourites',
  'stingray-ldap-access',
  'address-lookup',
  'ecom',
  'receipts',
  'external-orders',
  'phone-verification',
  'abandoned-carts',
  'cast-iron',
  'apple-pay-merchant-validation',
  'email-verification',
  'leads',
  'fixedposapi',
#   'sites-integration',
#   'inventory-integration',
#   'customer-transactions',
 ]

for api_name in apiList:
    try:
        responseProd = requests.get(prodUrl(api_name)).json()
        responsePreprod = requests.get(preprodUrl(api_name)).json()
        print(api_name + ': ' + responseProd['build_version'] + ' ' + responsePreprod['build_version'])
        # with open(service_name,'w') as file:
        #     file.writelines(api_name + ': ' + responseProd['build_version'] + ' ' + responsePreprod['build_version'] + '\n') 
    except:
        print (api_name + ' exception')

