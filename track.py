import random


class Track:
    def __init__(self,song_name=None,song_artist=None,song_image=None,song_prev_url=None):
        self.song_name = song_name
        self.song_artist = song_artist
        self.song_image = song_image
        self.song_prev_url = song_prev_url

    def get_song_name(self):
        return self.song_name
        
    def get_song_artist(self):
        return self.song_artist
        
    def get_song_image(self):
        return self.song_image
        
    def get_song_prev_url(self):
        return self.song_prev_url


#------------------END OF CLASS----------------------#


#---------------Start of Helper functions related to the class--------------------#

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

        
        
    














