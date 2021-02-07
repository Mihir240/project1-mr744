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
 
 #### Installtaion
 1) `pip install requests` or `sudo pip install requests`

 #### Setup
 1) Head over to www.spotify.com to create a free user account! Then follow these [instructions](https://developer.spotify.com/documentation/general/guides/app-settings/) for registering your application.
 2) Once you have followed the steps above you will access to the spotify `Client ID` and `Secret Key`. These will be available in your [spotify dev account dashboard!](https://developer.spotify.com/dashboard/login)
 3) Once you have those credentials you can follow the [Client Crenditals Flow](https://developer.spotify.com/documentation/general/guides/authorization-guide/) for authorization purposes.
 4) Next, use the Artists API to get the JSON format for the top ten tracks for an artist. [Top Tracks Documentation Here!](https://developer.spotify.com/documentation/web-api/reference/#category-artists)
 5) Additionally, from the Artists API we can retrieve info like the artist name, song name, preview url and song image.
 
 #### References
 1) [Official Spotify Web API Docs](https://developer.spotify.com/documentation/web-api/)
 2) [Client Credenitals Flow Hint](https://stmorse.github.io/journal/spotify-api.html)

### Spotipy (Optional)
---
 #### About
 Spotipy is a lightweight Python library which will help us retrieve the JSON metadata from the Spotify Web API. Instead of manually setting up the POST and Get methods in 
 Python we can use the this library to simply retrieve the JSON data as an alternative to the previous setup mentioned in Spotify Web API section.
 
 #### Installation
 1) `pip install spotipy --upgrade`
 
 #### Setup
 1) Follow the steps in the [Docs](https://spotipy.readthedocs.io/en/2.16.1/#client-credentials-flow) to setup the Client Credentials Flow.
 2) Refer to [API reference](https://spotipy.readthedocs.io/en/2.16.1/#api-reference) on how to retrieve the JSON format as neeed
 
 
### Hiding your Client ID and Secret Key via the .env file
---
  ### Installation
  1) `sudo pip install -U python-dotenv`

  ### Setup
  1) Create a `.env` file in you project folder which is in the same directory as your `cred.py` file
  2) In the file `.env` write the following:
     1. `export client_id='your client id'`
     2. `export client_secret='your client secret'`
  3) In `cred.py` import and include the following:
     1. `from dotenv import load_dotenv, find_dotenv`
     2. `import os`
     3. `load_dotenv(find_dotenv())`
     4. `os.getenv('cliend_id')`
     5. `os.getenv('client_secret')`
   4) Don't forget to add your `.env` file to the `.gitignore` file
   
   
## 3 Technical Issue Encountered in My Project and Fixes
1) One simple mistake but was quite time consuming mistake I faced was forgetting to add the line `load_dotenv(find_dotenv())` in my `cred.py` file. This caused much frustration 
   because I was getting invalid credential errors and was therefore not able to access the Web API. To resolve this issue, I first hardcoded my client_secret and client_id to 
   see if they would work and fortunately they worked. So I quickly realized that something was wrong in my .env file and maybe I spelt the variables wrong. But that wasn't the
   case. I then rewatched the Demo on 'Hiding our API Keys' and soon realized that I was missing the `load_dotenv(find_dotenv())` in my `cred.py`.

2) On Cloud9, whenever I updated my CSS file, the Html never updated. So the first step I took was to check if the CSS syntax was all good. And upon reviewing, the syntax was 
   all good. Then I went over to Slack to see if anyone else was facing similar issues. And several students were having similar issues and in a pinned post it said that we had
   to hard refresh our browser page to ensure the CSS got updated. So all we had to do was `CTRL F5` on windows to update the CSS!
   
3) 


## Known Problems



## Improving the Project in the future
 
 
  


