from flask import Flask, render_template
import os, random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from cred import spot_obj
from track import *

app = Flask(__name__)


@app.route('/')
def main_app():
    
    #spotify object that handles the get requests
    spotify_obj = spot_obj()
    
    #id's for fav artists
    id_artists = ['3TVXtAsR1Inumwj472S9r4', #drake
                '1Xyo4u8uXC1ZmMpatF05PJ', #weeknd
                '246dkjvS1zLTtiykXe5h60', #post malone
                '4dpARuHxo51G3z768sgnrY', #adele
                '163tK9Wjr9P9DmM0AVK7lm', #lorde
                '06HL4z0CvFAxyc27GXpf02', #taylor swift
                '6eUKZXaKkcviH0Ku9w2n3V'] #ed sheeran
    
    #chooses one id artist from the list
    selected_id = random.choice(id_artists)
    json_obj = spotify_obj.artist_top_tracks(selected_id,country='US')
    list_of_tracks = extract_track_info(json_obj)
    
    #retrieving artist info
    artist = spotify_obj.artist(selected_id)
                        # artist pic                 #artist name
    info_of_artist = [artist['images'][2]['url'], artist['name'], artist['popularity']]

    return render_template(
        'index.html',
        all_tracks = list_of_tracks,
        artist_info = info_of_artist,
    )

app.run(
    port = int(os.getenv('PORT',8080)),
    host = os.getenv('IP','0.0.0.0'),
    debug = True
)