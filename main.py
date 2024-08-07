import spotipy
from spotipy.oauth2 import SpotifyOAuth
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Enter your credentials that is obtained by creating spotify developer account
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id='', 
    client_secret='',
    redirect_uri='',
    scope='playlist-modify-private'))
user_id = sp.me()['id']
def get_mood(sentence):
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(sentence)
    if sentiment['compound'] >= 0.03:
        return 'positive'
    elif sentiment['compound'] <= -0.03:
        return 'negative'
    else:
        return 'neutral'
def get_tracks(sp, mood):
    if mood == 'positive':
        query = 'happy'
    elif mood == 'negative':
        query = 'sad'
    else:
        query = 'chill'
    results = sp.search(q=query, type='track', limit=10)
    tracks = [track['uri'] for track in results['tracks']['items']]
    return tracks

def create_playlist(sp, user_id, mood):
    playlist_name = f'{mood.capitalize()} Mood Playlist'
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
    return playlist['id']

def add_tracks_to_playlist(sp, playlist_id, tracks):
    sp.playlist_add_items(playlist_id, tracks)

def create_mood_based_playlist(sentence):
    mood = get_mood(sentence)
    tracks = get_tracks(sp, mood)
    playlist_id = create_playlist(sp, user_id, mood)
    add_tracks_to_playlist(sp, playlist_id, tracks)
    print(f'Private playlist created: {playlist_id}')

sentence = input("Explain your mood in a few sentences: ")
create_mood_based_playlist(sentence)
