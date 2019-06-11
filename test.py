
import requests
base_url = 'http://127.0.0.1:4455/'
endpoint_url = 'api/emp/'

final_url = base_url + endpoint_url
# resp = requests.get(final_url)
# print(resp.json())



pdata = {
    'product_number' : 60,
    'product_name' : 'IPhone',
    'product_class' : 'Good',
    'product_cost' : 95000,
    'product_weight' : 150,
}

# resp = requests.post(final_url,pdata)
# resp = requests.put(final_url+'5'+'/',pdata)
# resp = requests.delete(final_url+'id'+'/')
# resp = requests.get(final_url+'id'+'/')


# Using Djngo URLs
resp = requests.get('http://127.0.0.1:4455/retrieve/') # from django url
# resp = requests.post('http://127.0.0.1:4455/create/' , pdata) # from django url


#Using REST API  URLs
# resp = requests.get('http://127.0.0.1:4455/api/emp/') # from Restapi url
# resp = requests.post('http://127.0.0.1:4455/api/emp/', pdata) # from Restapi url



if resp.status_code==200 :
    print("Status code is: ",resp.status_code)
    try:
        print(resp.json())
    except:
        print('sorry, You are not getting the Json Response from Provider App')

elif resp.status_code==201:
    print("Status code is: ",resp.status_code)
    print(resp.json())
    print('Record created successfuly')

elif resp.status_code == 204:
    print("Status code is: ",resp.status_code)
    print('Record deleted successfully')

elif resp.status_code ==400:
    print("Status code is: ",resp.status_code)
    print('Bad request, Record not created')

elif resp.status_code == 404:
    print("Status code is: ",resp.status_code)
    print('Record not found')

elif resp.status_code == 403:
    print("Status code is: ",resp.status_code)
    print('Method not hitting, csrf token not available')

elif resp.status_code == 500:
    print("Status code is: ",resp.status_code)
    print('Server side exception')

else:
    print("Status code is: ",resp.status_code)
    print('sry unable to do this operation')

