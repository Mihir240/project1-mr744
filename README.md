# Project 1 - Spotify Web App

This repository consists of python, html and css files which will allow users to dynamically retrieve and display 3 songs
from a variety of artists of their choosing! 

## Getting Started - Techonologies

In this project, I used the Flask Framework, Spotify Web API, and Spotipy library. Additiionally, I used the python-dotnev and requests packages.

### Flask 
---
 #### About
 Flask is a lightweight web framework which will help us connect our Python code to our frontend. It does this using
   the templating language called Jinja2 which is used to create HTML or other markup formats.
   
 #### Installation
 1) `sudo pip install flask` or `pip install flask`
    
 #### Setup
 1) In my case, since I was using the Cloud9 IDE, I setup the Flask framework boiler plate code with the endpoint "/" and
    `'IP'` and `'PORT'` values set to `'0.0.0.0'` and `8080` respectively. Please refer to [Flask on Cloud9](https://damyan.blog/post/getting-started-with-flask-on-cloud9/)!

 2) If you are not using the Cloud9 IDE or you are just stuck, you can still use refer to the Official Documentation at any point in time. 
    Please refer to the [Official Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/)!
 
### Spotify Web API
---
 #### About
 The Spotify Web API essentially allows us to use its endpoints to retreive JSON metadata about music artists, albums, and
 tracks, directly from the Spotify Data Catalogue. The API is based on the [REST Principles](https://restfulapi.net/)!

 #### Setup
 1) Head over to www.spotify.com to create a free user account! Then follow these [instructions](https://developer.spotify.com/documentation/general/guides/app-settings/) for registering your application.
 2) Once you have followed the steps above you will access to the spotify `Client ID` and `Secret Key`. These will be available in your [spotify dev account dashboard!](https://developer.spotify.com/dashboard/login)
 3) Once you have those credentials you can follow the [Client Crenditals Flow](https://developer.spotify.com/documentation/general/guides/authorization-guide/) for authorization purposes.
 4) Next, use the Artists API to get the JSON format for the top ten tracks for an artist. [Top Tracks Documentation Here!](https://developer.spotify.com/documentation/web-api/reference/#category-artists)
 5) Additionally, from the Artists API we can retrieve info like the artist name, song name, preview url and song image.
 
 #### References
 1) [Official Spotify Web API Docs](https://developer.spotify.com/documentation/web-api/)
 2) [Client Credenitals Flow Hint](https://stmorse.github.io/journal/spotify-api.html)

### Spotipy
---
-
  
  #### Installation
 
  


