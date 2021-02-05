from flask import Flask, render_template
import os, random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from cred import spot_obj
from track import *

app = Flask(__name__)

def extract_track_info(json_obj: dict) -> list:
    all_tracks = []
    
    #traverse the json_obj
    for info in json_obj['tracks'][:3]:
        print(f"Song artist: {info['artists'][0]['name']}")
        print(f"Song name: {info['name']} ")
        print(f"Song image: {info['album']['images'][2]['url']}")
        print(f"Song preview url: {info['preview_url']}")
        print(" ")
        
        song_artist = info['artists'][0]['name']
        song_name = info['name']
        song_image = info['album']['images'][2]['url']
        song_url = info['preview_url']
        
        
        all_tracks.append(
            Track(song_name,
                song_artist,
                song_image,
                song_url,
                )
            )
        
    return all_tracks
    
@app.route('/')
def main_app():
    
    # client_credentials_manager = SpotifyClientCredentials(client_id=os.getenv("client_id"), client_secret=os.getenv("client_secret"))
    # sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    
    #spotify object handle
    sp = spot_obj()
    
                  #drake, weeknd, post malone, adele, lorde
    id_artists = ['3TVXtAsR1Inumwj472S9r4','1Xyo4u8uXC1ZmMpatF05PJ','246dkjvS1zLTtiykXe5h60','4dpARuHxo51G3z768sgnrY','163tK9Wjr9P9DmM0AVK7lm']
    
    #choose one id artist from the array
    selected_id = random.choice(id_artists)
    
    #pass json format in the track obj
    json_obj = sp.artist_top_tracks(selected_id,country='US')
    
    
    
    #pass it into 
    list_of_tracks = extract_track_info(json_obj)
    
    
    # print(sp.artist_top_tracks("1Xyo4u8uXC1ZmMpatF05PJ", country='US'))
    # print(json_obj)
    print(list_of_tracks[0].get_song_name())
    print(list_of_tracks[0].get_song_artist())
    print(list_of_tracks[0].get_song_image())
    print(list_of_tracks[0].get_song_prev_url())
    
    return render_template(
        'index.html',
    )

app.run(
    port = int(os.getenv('PORT',8080)),
    host = os.getenv('IP','0.0.0.0'),
    debug = True
)