import os
from dotenv import load_dotenv, find_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv(find_dotenv())

#return spotify object to retrieve certain json data formats
def spot_obj():
    client_credentials_manager = SpotifyClientCredentials(client_id=os.getenv("client_id"), client_secret=os.getenv("client_secret"))
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    return sp