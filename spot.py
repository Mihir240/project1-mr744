import requests
import os
import json
from dotenv import load_dotenv, find_dotenv


class Spotify:
    def __init__(self, url: str, client_id: str, client_secret: str):
        self.url = url
        self.client_id = client_id
        self.client_secret = client_secret
        
    def get_token(self) -> str:
        params={
        'grant_type' : 'client_credentials',
        'client_id': self.client_id,
        'client_secret': self.client_secret,
        }

        #create an access token for spotify
        response = requests.post(
            self.url,
            data=params
        )

        #retrieve our token
        return response.json()['access_token']
    
                
                
            








