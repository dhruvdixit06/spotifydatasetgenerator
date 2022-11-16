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
    spotify_albums['duration_ms']=[]
    spotify_albums['key']=[]
    spotify_albums['mode']=[]
    spotify_albums['track image']=[]
    spotify_albums['song_url']=[]
    spotify_albums['album type']=[]
    spotify_albums['album name']=[]
    results = sp.search(q,limit=None)
    for idx, track in enumerate(results['tracks']['items']):
        song_id = results['tracks']['items'][idx]['id']
        artist=[]
        pop = sp.track(song_id)
        for i in pop["artists"]:
            artist.append(i['name'])
        #pull audio features per track
        features = sp.audio_features(song_id) 
        #Append to relevant key-value
        spotify_albums['duration_ms'].append(features[0]['duration_ms'])
        spotify_albums['key'].append(features[0]['key'])
        spotify_albums['mode'].append(features[0]['mode'])
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
        spotify_albums['popularity'].append(pop['popularity'])
        #etc
        spotify_albums['song_url'].append(pop['external_urls']['spotify'])
        spotify_albums['album name'].append(pop['album']['name'])
        spotify_albums['album type'].append(pop['album']['album_type'])
        spotify_albums['track image'].append(pop['album']['images'][0]['url'])
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
    dic_df['duration_ms']=[]
    dic_df['key']=[]
    dic_df['mode']=[]
    dic_df['track image']=[]
    dic_df['album type']=[]
    dic_df['album name']=[]
    dic_df['song_url']=[]
    for t in spotify_albums: 
            dic_df[t].extend(spotify_albums[t])
    dataframe = pd.DataFrame.from_dict(dic_df)
    return dataframe

def Song(q,client_id_in,client_secret_in):
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
        spotify_albums['duration_ms']=[]
        spotify_albums['key']=[]
        spotify_albums['mode']=[]
        spotify_albums['track image']=[]
        spotify_albums['song_url']=[]
        spotify_albums['album type']=[]
        spotify_albums['album name']=[]
        results=sp.track(q)
        artist=[]
        song_id = results['id']
        pop = sp.track(song_id)
        for i in pop["artists"]:
               artist.append(i['name'])
        #pull audio features per track
        features = sp.audio_features(song_id) 
        #Append to relevant key-value
        spotify_albums['duration_ms'].append(features[0]['duration_ms'])
        spotify_albums['key'].append(features[0]['key'])
        spotify_albums['mode'].append(features[0]['mode'])
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
        spotify_albums['popularity'].append(pop['popularity'])
        #etc
        spotify_albums['song_url'].append(pop['external_urls']['spotify'])
        spotify_albums['album name'].append(pop['album']['name'])
        spotify_albums['album type'].append(pop['album']['album_type'])
        spotify_albums['track image'].append(pop['album']['images'][0]['url'])
        spotify_albums['song_uri'].append("spotify:track:"+song_id)
        spotify_albums['song_id'].append(song_id)
        spotify_albums['track name'].append(results['name'])
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
        dic_df['duration_ms']=[]
        dic_df['key']=[]
        dic_df['mode']=[]
        dic_df['track image']=[]
        dic_df['album type']=[]
        dic_df['album name']=[]
        dic_df['song_url']=[]
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
        spotify_albums['duration_ms']=[]
        spotify_albums['key']=[]
        spotify_albums['mode']=[]
        spotify_albums['track image']=[]
        spotify_albums['song_url']=[]
        spotify_albums['album type']=[]
        spotify_albums['album name']=[]
        results=sp.playlist_tracks(q)
        for track in results['items']:
            song_id = track['track']['id']
            artist=[]
            song_id = track['track']['id']
            pop = sp.track(song_id)
            for i in pop["artists"]:
                artist.append(i['name'])
            #pull audio features per track
            features = sp.audio_features(song_id) 
            #Append to relevant key-value
            spotify_albums['duration_ms'].append(features[0]['duration_ms'])
            spotify_albums['key'].append(features[0]['key'])
            spotify_albums['mode'].append(features[0]['mode'])
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
            spotify_albums['popularity'].append(pop['popularity'])
            #etc
            spotify_albums['song_url'].append(pop['external_urls']['spotify'])
            spotify_albums['album name'].append(pop['album']['name'])
            spotify_albums['album type'].append(pop['album']['album_type'])
            spotify_albums['track image'].append(pop['album']['images'][0]['url'])
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
        dic_df['duration_ms']=[]
        dic_df['key']=[]
        dic_df['mode']=[]
        dic_df['track image']=[]
        dic_df['album type']=[]
        dic_df['album name']=[]
        dic_df['song_url']=[]
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
        spotify_albums['duration_ms']=[]
        spotify_albums['key']=[]
        spotify_albums['mode']=[]
        spotify_albums['track image']=[]
        spotify_albums['song_url']=[]
        spotify_albums['album type']=[]
        spotify_albums['album name']=[]
        results=sp.album_tracks(q)
        for track in results['items']:
            song_id = track['id']
            artist=[]
            pop = sp.track(song_id)
            for i in pop["artists"]:
                artist.append(i['name'])
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
            spotify_albums['duration_ms'].append(features[0]['duration_ms'])
            spotify_albums['key'].append(features[0]['key'])
            spotify_albums['mode'].append(features[0]['mode'])
            #popularity is stored elsewhere
            spotify_albums['popularity'].append(pop['popularity'])
            #etc
            spotify_albums['song_url'].append(pop['external_urls']['spotify'])
            spotify_albums['album name'].append(pop['album']['name'])
            spotify_albums['album type'].append(pop['album']['album_type'])
            spotify_albums['track image'].append(pop['album']['images'][0]['url'])
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
        dic_df['duration_ms']=[]
        dic_df['key']=[]
        dic_df['mode']=[]
        dic_df['track image']=[]
        dic_df['album type']=[]
        dic_df['album name']=[]
        dic_df['song_url']=[]
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
        spotify_albums['duration_ms']=[]
        spotify_albums['key']=[]
        spotify_albums['mode']=[]
        spotify_albums['track image']=[]
        spotify_albums['song_url']=[]
        spotify_albums['album type']=[]
        spotify_albums['album name']=[]
        result = sp.search(q, type='artist')
        id = result['artists']['items'][0]['id']
        res2=sp.artist(id)
        name=res2['name']
        print(name)
        albums = sp.artist_albums(id)
        for album in albums['items']:
            album_id = album['id']
            results=sp.album_tracks(album_id)
            for track in results['items']:
                song_id = track['id']
                artist=[]
                pop = sp.track(song_id)
                for i in pop["artists"]:
                    artist.append(i['name'])
                if name not in artist:
                    continue
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
                spotify_albums['duration_ms'].append(features[0]['duration_ms'])
                spotify_albums['key'].append(features[0]['key'])
                spotify_albums['mode'].append(features[0]['mode'])
                #popularity is stored elsewhere
                spotify_albums['popularity'].append(pop['popularity'])
                #etc
                spotify_albums['song_url'].append(pop['external_urls']['spotify'])
                spotify_albums['album name'].append(pop['album']['name'])
                spotify_albums['album type'].append(pop['album']['album_type'])
                spotify_albums['track image'].append(pop['album']['images'][0]['url'])
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
        dic_df['duration_ms']=[]
        dic_df['key']=[]
        dic_df['mode']=[]
        dic_df['track image']=[]
        dic_df['album type']=[]
        dic_df['album name']=[]
        dic_df['song_url']=[]
        for t in spotify_albums: 
                dic_df[t].extend(spotify_albums[t])
        dataframe = pd.DataFrame.from_dict(dic_df)
        return dataframe
    
client_id_in=st.text_input(label="Enter Spotify Client ID")
client_secret_in=st.text_input(label="Enter Spotify Client Secret",type="password")
type=st.selectbox(label="Select the type of query",options=("Search Query","Song Query", "Playlist Query","Album Query","Artist Query"))
if(type=="Search Query"):
    q=st.text_input(label="Enter Search Query")

elif(type=="Song Query"):
    q=st.text_input(label="Enter Song URI")

elif(type=="Playlist Query"):
    q=st.text_input(label="Enter Playlist URI")

elif(type=="Album Query"):
    q=st.text_input(label="Enter Album URI")

elif(type=="Artist Query"):
    q=st.text_input(label="Enter Artist Name")

if st.button('Enter'):
    if(type=="Search Query" and q!=""):
        dataframe=Search(q,client_id_in,client_secret_in)

    elif(type=="Song Query" and q!=""):
        dataframe=Song(q,client_id_in,client_secret_in)

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