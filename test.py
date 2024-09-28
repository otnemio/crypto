import hashlib
import hmac
import yaml, os
import requests
import datetime

def init():
    global api_key,api_secret
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with open("cred.yaml","r") as stream:
            cred = yaml.safe_load(stream)
            api_key = cred['api_key']
            api_secret = cred['api_secret']

def generate_signature(secret, message):
    message = bytes(message, 'utf-8')
    secret = bytes(secret, 'utf-8')
    hash = hmac.new(secret, message, hashlib.sha256)
    return hash.hexdigest()

def get_time_stamp():
    d = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
    epoch = datetime.datetime(1970,1,1)
    return str(int((d - epoch).total_seconds()))

url = "https://api.india.delta.exchange/v2/orders/"

# Get open orders
def get_open_orders():
    payload = ''
    method = 'GET'
    timestamp = get_time_stamp()
    path = '/v2/orders'
    query_string = '?product_id=1&state=open'
    signature_data = method + timestamp + path + query_string + payload
    signature = generate_signature(api_secret, signature_data)

    req_headers = {
    'api-key': api_key,
    'timestamp': timestamp,
    'signature': signature,
    'User-Agent': 'rest-client',
    'Content-Type': 'application/json'
    }
    query = {"product_id": 1, "state": 'open'}

    response = requests.request(
        method, url, data=payload, params=query, timeout=(3, 27), headers=req_headers
    )
    print(response.status_code)

# Place new order
def place_new_order():
    method = 'POST'
    timestamp = get_time_stamp()
    path = '/v2/orders'
    query_string = ''
    payload = "{\"order_type\":\"limit_order\",\"size\":3,\"side\":\"buy\",\"limit_price\":\"0.0005\",\"product_id\":16}"
    signature_data = method + timestamp + path + query_string + payload
    signature = generate_signature(api_secret, signature_data)

    req_headers = {
    'api-key': api_key,
    'timestamp': timestamp,
    'signature': signature,
    'User-Agent': 'rest-client',
    'Content-Type': 'application/json'
    }

    response = requests.request(
        method, url, data=payload, params={}, timeout=(3, 27), headers=req_headers
    )
    print(response.status_code)

def get_balance():
    payload = ''
    method = 'GET'
    timestamp = get_time_stamp()
    path = '/v2/wallet/balances'
    query_string = ''
    signature_data = method + timestamp + path + query_string + payload
    signature = generate_signature(api_secret, signature_data)

    headers = {
    'Accept': 'application/json',
    'api-key': api_key,
    'signature': signature,
    'timestamp': timestamp
    }

    r = requests.get('https://api.india.delta.exchange/v2/wallet/balances', params={

    }, headers = headers)

    print (r.json())

init()
get_balance()