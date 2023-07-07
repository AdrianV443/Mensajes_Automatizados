import os
from twilio.rest import Client
from twilio_config import *
import time
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import requests
from datetime import datetime
from utils import request_cripto,get_prices,create_df,send_message,get_date



api_key = API_KEY

input_date= get_date()
data = request_cripto(api_key)

datos = []

for i in data['data']:
    datos.append(get_prices(reponse))


df = create_df(datos)

# Send Message
message_id = send_message(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,input_date,df)


print('Mensaje Enviado con exito ' + message_id)