from flask import Flask, render_template
import os, random
from spot import *

app = Flask(__name__)

@app.route('/')
def main_app():
    
    url = 'https://accounts.spotify.com/api/token'
    
    #retrieve token
    spot_obj = Spotify(url, os.getenv("client_id"), os.getenv("client_secret"))
    token = spot_obj.get_token()
    
    #I am going to add this in my newclass branch
    
    # print(f'The token is: {token}')
    
    #initialize top ten artists
    
    
    return render_template(
        'index.html',
    )

app.run(
    port = int(os.getenv('PORT',8080)),
    host = os.getenv('IP','0.0.0.0'),
    debug = True
)