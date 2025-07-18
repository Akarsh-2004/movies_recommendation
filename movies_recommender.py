import pandas as pd
import joblib

df = pd.read_csv('./movies_recommendationzip/movies.csv')
df['genres'] = df['genres'].fillna('').apply(lambda x: x.replace('|', ' '))

tfidf = joblib.load('tfidf_vectorizer.pkl')
knn = joblib.load('knn_model.pkl')

tfidf_matrix = tfidf.transform(df['genres'])

from difflib import get_close_matches

def recommend_movies(title=None, genre=None, n_recs=5):
    if title:
        title = title.lower()
        
        # Find closest match using fuzzy matching
        all_titles = df['title'].str.lower().tolist()
        matches = get_close_matches(title, all_titles, n=1, cutoff=0.3)

        if not matches:
            return " Title not found in the dataset."

        best_match = matches[0]
        idx = df[df['title'].str.lower() == best_match].index[0]

        distances, indices = knn.kneighbors(tfidf_matrix[idx], n_neighbors=n_recs + 1)
        recs = df.iloc[indices[0][1:]]['title'].tolist()
        return recs

    elif genre:
        genre = genre.replace('|', ' ')
        genre_vector = tfidf.transform([genre])
        distances, indices = knn.kneighbors(genre_vector, n_neighbors=n_recs)
        recs = df.iloc[indices[0]]['title'].tolist()
        return recs

    else:
        return "Please provide at least a title or genre."
