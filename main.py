from flask import Flask, render_template
import os, random
from spot import *
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)


@app.route('/')
def main_app():
    
    client_credentials_manager = SpotifyClientCredentials(client_id=os.getenv("client_id"), client_secret=os.getenv("client_secret"))
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    print(sp.artist_top_tracks("1Xyo4u8uXC1ZmMpatF05PJ", country='US'))
    
    
    return render_template(
        'index.html',
    )

app.run(
    port = int(os.getenv('PORT',8080)),
    host = os.getenv('IP','0.0.0.0'),
    debug = True
)