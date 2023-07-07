import pandas as pd
from twilio.rest import Client
from twilio_config import TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,PHONE_NUMBER,API_KEY
from datetime import datetime
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json



def get_date():

    input_date = datetime.now()
    input_date = input_date.strftime("%Y-%m-%d")

    return input_date

def request_cripto(api_key):   
    
    url_clima = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    
    parameters = {"start": "1",
                  "limit": "10",
                  "convert": "USD"}
    
    headers = {"X-CMC_PRO_API_KEY": api_key}
    
    try :
        response = requests.get(url, params=parameters, headers=headers).json()
    except Exception as e:
        print(e)
    return response

def get_prices(response):
    
    nombre = response['name']
    precio = response['quote']['USD']['price']
    
    return nombre,precio

def create_df(data):
    
    col = ['Cripto','Precio']
    df = pd.DataFrame(data,columns=col)
    
    return df  
    
def send_message(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,input_date,df):
    
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body='\nHola! \n\n\n Este es el top 10 de cirptomonedas del día de hoy: '+ input_date +' \n\n\n ' + str(df),
                        from_=PHONE_NUMBER,
                        to='whatsapp:+5217751425295'
                    )

    return message.sid