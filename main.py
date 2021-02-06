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
    for info in json_obj['tracks'][:10]:

        song_artist = info['artists'][0]['name']
        song_name = info['name']
        song_image = info['album']['images'][1]['url']
        song_url = info['preview_url']
        
        
        all_tracks.append(
            Track(song_name,
                song_artist,
                song_image,
                song_url,
                )
            )
            
    return random.sample(all_tracks,3)

@app.route('/')
def main_app():
    
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
    
    
    artist = sp.artist(selected_id)
    #artist image url
    image_of_artist = artist['images'][2]['url']
    
    #artist name
    artist_name = artist['name']
    
    print(image_of_artist)
    return render_template(
        'index.html',
        all_tracks = list_of_tracks,
        url_artist = image_of_artist,
        artist_name = artist_name,
    )

app.run(
    port = int(os.getenv('PORT',8080)),
    host = os.getenv('IP','0.0.0.0'),
    debug = True
)