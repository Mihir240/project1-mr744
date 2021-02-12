import os, requests, json
from dotenv import load_dotenv, find_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv(find_dotenv())

#return spotify object to retrieve certain json data formats
def spot_obj():
    client_credentials_manager = SpotifyClientCredentials(client_id=os.getenv("client_id"), client_secret=os.getenv("client_secret"))
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    return sp
    
def gen_obj(song_name=None)->str:
    
    # song_name = "better now"
    url = f"https://api.genius.com/search?q={song_name}"
    
    headers = {
        'Authorization': f"Bearer {os.getenv('gen_client_token')}"
    }
    
    song_lyrics = requests.get(
        url=url,
        headers=headers,
        )
    #get the song lyrics url 
    lyrics = song_lyrics.json()['response']['hits'][0]['result']['url']
    return lyrics

gen_obj("Better Now")