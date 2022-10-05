import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

st.set_page_config(page_title="Produce Dataset", page_icon="📑",layout="wide")
st.title(" Produce Dataset")


def Search(q,client_id_in,client_secret_in):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id_in,
                                                           client_secret=client_secret_in))
    spotify_albums={}
    spotify_albums['song_id']=[]
    spotify_albums['song_uri']=[]
    spotify_albums['artist']=[]
    spotify_albums['acousticness'] = []
    spotify_albums['danceability'] = []
    spotify_albums['energy'] = []
    spotify_albums['instrumentalness'] = []
    spotify_albums['liveness'] = []
    spotify_albums['loudness'] = []
    spotify_albums['speechiness'] = []
    spotify_albums['tempo'] = []
    spotify_albums['valence'] = []
    spotify_albums['popularity'] = []
    spotify_albums['track name']=[]
    results = sp.search(q,limit=None)
    for idx, track in enumerate(results['tracks']['items']):
        song_id = results['tracks']['items'][idx]['id']
        artist = track['artists'][0]['name']
        #pull audio features per track
        features = sp.audio_features(song_id) 
        #Append to relevant key-value
        spotify_albums['acousticness'].append(features[0]['acousticness'])
        spotify_albums['danceability'].append(features[0]['danceability'])
        spotify_albums['energy'].append(features[0]['energy'])
        spotify_albums['instrumentalness'].append(features[0]['instrumentalness'])
        spotify_albums['liveness'].append(features[0]['liveness'])
        spotify_albums['loudness'].append(features[0]['loudness'])
        spotify_albums['speechiness'].append(features[0]['speechiness'])
        spotify_albums['tempo'].append(features[0]['tempo'])
        spotify_albums['valence'].append(features[0]['valence'])
        #popularity is stored elsewhere
        pop = sp.track(song_id)
        spotify_albums['popularity'].append(pop['popularity'])
        #etc
        spotify_albums['song_uri'].append("spotify:track:"+song_id)
        spotify_albums['song_id'].append(song_id)
        spotify_albums['track name'].append(track['name'])
        spotify_albums['artist'].append(artist)
    dic_df = {}
    dic_df['song_id'] = []
    dic_df['song_uri']=[]
    dic_df['track name'] = []
    dic_df['artist']=[]
    dic_df['acousticness'] = []
    dic_df['danceability'] = []
    dic_df['energy'] = []
    dic_df['instrumentalness'] = []
    dic_df['liveness'] = []
    dic_df['loudness'] = []
    dic_df['speechiness'] = []
    dic_df['tempo'] = []
    dic_df['valence'] = []
    dic_df['popularity'] = []
    for t in spotify_albums: 
            dic_df[t].extend(spotify_albums[t])
    dataframe = pd.DataFrame.from_dict(dic_df)
    return dataframe

def Playlist(q,client_id_in,client_secret_in):
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id_in,
                                                           client_secret=client_secret_in))
        spotify_albums={}
        spotify_albums['song_id']=[]
        spotify_albums['song_uri']=[]
        spotify_albums['artist']=[]
        spotify_albums['acousticness'] = []
        spotify_albums['danceability'] = []
        spotify_albums['energy'] = []
        spotify_albums['instrumentalness'] = []
        spotify_albums['liveness'] = []
        spotify_albums['loudness'] = []
        spotify_albums['speechiness'] = []
        spotify_albums['tempo'] = []
        spotify_albums['valence'] = []
        spotify_albums['popularity'] = []
        spotify_albums['track name']=[]
        results=sp.playlist_tracks(q)
        for track in results['items']:
            song_id = track['track']['id']
            artist = track["track"]["artists"][0]["name"]
            #pull audio features per track
            features = sp.audio_features(song_id) 
            #Append to relevant key-value
            spotify_albums['acousticness'].append(features[0]['acousticness'])
            spotify_albums['danceability'].append(features[0]['danceability'])
            spotify_albums['energy'].append(features[0]['energy'])
            spotify_albums['instrumentalness'].append(features[0]['instrumentalness'])
            spotify_albums['liveness'].append(features[0]['liveness'])
            spotify_albums['loudness'].append(features[0]['loudness'])
            spotify_albums['speechiness'].append(features[0]['speechiness'])
            spotify_albums['tempo'].append(features[0]['tempo'])
            spotify_albums['valence'].append(features[0]['valence'])
            #popularity is stored elsewhere
            pop = sp.track(song_id)
            spotify_albums['popularity'].append(pop['popularity'])
            #etc
            spotify_albums['song_uri'].append("spotify:track:"+song_id)
            spotify_albums['song_id'].append(song_id)
            spotify_albums['track name'].append(track['track']['name'])
            spotify_albums['artist'].append(artist)
        dic_df = {}
        dic_df['song_id'] = []
        dic_df['song_uri']=[]
        dic_df['track name'] = []
        dic_df['artist']=[]
        dic_df['acousticness'] = []
        dic_df['danceability'] = []
        dic_df['energy'] = []
        dic_df['instrumentalness'] = []
        dic_df['liveness'] = []
        dic_df['loudness'] = []
        dic_df['speechiness'] = []
        dic_df['tempo'] = []
        dic_df['valence'] = []
        dic_df['popularity'] = []
        for t in spotify_albums: 
                dic_df[t].extend(spotify_albums[t])
        dataframe = pd.DataFrame.from_dict(dic_df)
        return dataframe

def Album(q,client_id_in,client_secret_in):
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id_in,
                                                           client_secret=client_secret_in))
        spotify_albums={}
        spotify_albums['song_id']=[]
        spotify_albums['song_uri']=[]
        spotify_albums['artist']=[]
        spotify_albums['acousticness'] = []
        spotify_albums['danceability'] = []
        spotify_albums['energy'] = []
        spotify_albums['instrumentalness'] = []
        spotify_albums['liveness'] = []
        spotify_albums['loudness'] = []
        spotify_albums['speechiness'] = []
        spotify_albums['tempo'] = []
        spotify_albums['valence'] = []
        spotify_albums['popularity'] = []
        spotify_albums['track name']=[]
        results=sp.album_tracks(q)
        for track in results['items']:
            song_id = track['id']
            artist = track["artists"][0]["name"]
            #pull audio features per track
            features = sp.audio_features(song_id) 
            #Append to relevant key-value
            spotify_albums['acousticness'].append(features[0]['acousticness'])
            spotify_albums['danceability'].append(features[0]['danceability'])
            spotify_albums['energy'].append(features[0]['energy'])
            spotify_albums['instrumentalness'].append(features[0]['instrumentalness'])
            spotify_albums['liveness'].append(features[0]['liveness'])
            spotify_albums['loudness'].append(features[0]['loudness'])
            spotify_albums['speechiness'].append(features[0]['speechiness'])
            spotify_albums['tempo'].append(features[0]['tempo'])
            spotify_albums['valence'].append(features[0]['valence'])
            #popularity is stored elsewhere
            pop = sp.track(song_id)
            spotify_albums['popularity'].append(pop['popularity'])
            #etc
            spotify_albums['song_uri'].append("spotify:track:"+song_id)
            spotify_albums['song_id'].append(song_id)
            spotify_albums['track name'].append(track['name'])
            spotify_albums['artist'].append(artist)
        dic_df = {}
        dic_df['song_id'] = []
        dic_df['song_uri']=[]
        dic_df['track name'] = []
        dic_df['artist']=[]
        dic_df['acousticness'] = []
        dic_df['danceability'] = []
        dic_df['energy'] = []
        dic_df['instrumentalness'] = []
        dic_df['liveness'] = []
        dic_df['loudness'] = []
        dic_df['speechiness'] = []
        dic_df['tempo'] = []
        dic_df['valence'] = []
        dic_df['popularity'] = []
        for t in spotify_albums: 
                dic_df[t].extend(spotify_albums[t])
        dataframe = pd.DataFrame.from_dict(dic_df)
        return dataframe

def Artist(q,client_id_in,client_secret_in):
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id_in,
                                                           client_secret=client_secret_in))
        spotify_albums={}
        spotify_albums['song_id']=[]
        spotify_albums['song_uri']=[]
        spotify_albums['artist']=[]
        spotify_albums['acousticness'] = []
        spotify_albums['danceability'] = []
        spotify_albums['energy'] = []
        spotify_albums['instrumentalness'] = []
        spotify_albums['liveness'] = []
        spotify_albums['loudness'] = []
        spotify_albums['speechiness'] = []
        spotify_albums['tempo'] = []
        spotify_albums['valence'] = []
        spotify_albums['popularity'] = []
        spotify_albums['track name']=[]
        result = sp.search(q, type='artist')
        id = result['artists']['items'][0]['id']
        albums = sp.artist_albums(id)
        for album in albums['items']:
            album_id = albums['items'][0]['id']
            results=sp.album_tracks(album_id)
            for track in results['items']:
                song_id = track['id']
                artist = track["artists"][0]["name"]
                #pull audio features per track
                features = sp.audio_features(song_id) 
                #Append to relevant key-value
                spotify_albums['acousticness'].append(features[0]['acousticness'])
                spotify_albums['danceability'].append(features[0]['danceability'])
                spotify_albums['energy'].append(features[0]['energy'])
                spotify_albums['instrumentalness'].append(features[0]['instrumentalness'])
                spotify_albums['liveness'].append(features[0]['liveness'])
                spotify_albums['loudness'].append(features[0]['loudness'])
                spotify_albums['speechiness'].append(features[0]['speechiness'])
                spotify_albums['tempo'].append(features[0]['tempo'])
                spotify_albums['valence'].append(features[0]['valence'])
                #popularity is stored elsewhere
                pop = sp.track(song_id)
                spotify_albums['popularity'].append(pop['popularity'])
                #etc
                spotify_albums['song_uri'].append("spotify:track:"+song_id)
                spotify_albums['song_id'].append(song_id)
                spotify_albums['track name'].append(track['name'])
                spotify_albums['artist'].append(artist)
        dic_df = {}
        dic_df['song_id'] = []
        dic_df['song_uri']=[]
        dic_df['track name'] = []
        dic_df['artist']=[]
        dic_df['acousticness'] = []
        dic_df['danceability'] = []
        dic_df['energy'] = []
        dic_df['instrumentalness'] = []
        dic_df['liveness'] = []
        dic_df['loudness'] = []
        dic_df['speechiness'] = []
        dic_df['tempo'] = []
        dic_df['valence'] = []
        dic_df['popularity'] = []
        for t in spotify_albums: 
                dic_df[t].extend(spotify_albums[t])
        dataframe = pd.DataFrame.from_dict(dic_df)
        return dataframe
    
client_id_in=st.text_input(label="Enter Spotify Client ID")
client_secret_in=st.text_input(label="Enter Spotify Client Secret",type="password")
type=st.selectbox(label="Select the type of query",options=("Search Query", "Playlist Query","Album Query","Artist Query"))
if(type=="Search Query"):
    q=st.text_input(label="Enter Search Query")

elif(type=="Playlist Query"):
    q=st.text_input(label="Enter Playlist URI")

elif(type=="Album Query"):
    q=st.text_input(label="Enter Album URI")

elif(type=="Artist Query"):
    q=st.text_input(label="Enter Artist Name")

if st.button('Enter'):
    if(type=="Search Query" and q!=""):
        dataframe=Search(q,client_id_in,client_secret_in)

    elif(type=="Playlist Query" and q!=""):
        dataframe=Playlist(q,client_id_in,client_secret_in)

    elif(type=="Album Query" and q!=""):
        dataframe=Album(q,client_id_in,client_secret_in)

    elif(type=="Artist Query" and q!=""):
        dataframe=Artist(q,client_id_in,client_secret_in)
    csv=dataframe.to_csv().encode('utf-8')
    st.download_button(
        "Press to Download",
        csv,
        "file.csv",
        "text/csv",
        key='download-csv'
        )

st.subheader('Contact Developer:')
d='''
Dhruv Dixit❤️ \n
✅Github : https://github.com/dhruvdixit06 \n
✅LinkedIn : https://www.linkedin.com/in/dhruv-dixit/
'''
st.markdown(d,unsafe_allow_html=True)