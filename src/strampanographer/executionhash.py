import requests
import json
from api_key import api_key
RANDOM_API_URL = "https://api.random.org/json-rpc/4/invoke"


def generate_execution_hash():   
    json_string = create_json_string(api_key)
    
    response = http_request(RANDOM_API_URL, json_string)
    response_json = json.loads(response)
    
    return response_json.get("result").get("random").get("data")[0]

def create_json_string(api_key):
    jsondict = {
    "jsonrpc": "2.0",
    "method": "generateStrings",
    "params": {
        "apiKey": api_key,
        "n": 1,
        "length": 10,
        "characters": "abcdefghijklmnopqrstuvwxyz",
        "replacement": True
    },
    "id": 1314
    }   
    json_string = json.dumps(jsondict, indent=4)
    return json_string

def http_request(url, json_string):
    """
    Request data from server (POST)

    :param json_string: JSON-String
    """
    headers={"Content-Type" : "application/json"}
    
    request = requests.post(url, data=json_string, headers=headers)
    
    
    response_string = request.text
    request.close()

    return response_string