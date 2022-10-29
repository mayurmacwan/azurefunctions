import logging
import requests
import azure.functions as func
import re
import json

def cls_string(pro_string):
    return (pro_string.split(" ")[1])

def airwave_get_tokens():
    session = requests.Session()
    payload = {'destination': '/api',
               'credential_0': 'replacewithyourcred',
               'credential_1': 'replacewithyourpw'}
    r = session.post('https://replacewithyoururl/LOGIN', verify=False, data=payload)
    return session.cookies,r.headers['X-BISCOTTI']

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    cookies, delicious_biscotti = airwave_get_tokens()

    return func.HttpResponse(
            json.dumps({
            'cookie': cls_string(str(cookies)),
            'token': delicious_biscotti
 
            }) 
         )
