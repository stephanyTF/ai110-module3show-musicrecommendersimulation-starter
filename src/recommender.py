import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    # TODO: Implement CSV loading logic
    print(f"Loading songs from {csv_path}...")
    #read CSV and return list of song dictionaries
    songs = []
    with open(csv_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            songs.append(row)

    return songs

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)

    #scoring:
    for song in songs:
        user_genre = user_prefs['favorite_genre']
        song_genre = song['genre']
        if song_genre == user_genre:
            genre_match = 1.0  # exact match
        elif user_genre in song_genre or song_genre in user_genre:
            genre_match = 0.5  # partial match (e.g. "pop" in "indie pop")
        else:
            genre_match = 0.0
        mood_match = 1.0 if song['mood'] == user_prefs['favorite_mood'] else 0.0
        energy = float(song['energy'])
        acousticness = float(song['acousticness'])

        score = (2 * genre_match           # 1.0 match or 0.0 if not
        + mood_match             # 1.0 or 0.0
        + (1 - abs(energy - user_prefs['target_energy']))
        + (1 - abs(acousticness - user_prefs['likes_acoustic'])))
        song['score'] = score

    #rec_songs = sorted([(song, song['score'], "Explanation placeholder") for song in songs], key=lambda x: x[1], reverse=True)[:k] #compressed version of below code
    
    #create list of tuples (song, score, explanation) and sort by score

    rec_songs = []
    for song in songs:
        #song_title = song['title']
        score = song['score']
        explanation = "Explanation Placeholder"
        rec_songs.append((song, score, explanation))
    rec_songs = sorted(rec_songs, key=lambda x: x[1], reverse=True)[:k]

    return rec_songs   
