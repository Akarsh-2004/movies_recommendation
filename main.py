from fastapi import FastAPI, Query
from movies_recommender import recommend_movies
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Allow CORS for your frontend port (Vite: 5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://moviesideas.netlify.app"],  # <-- your Netlify domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/recommend/")
def recommend(title: str = None, genre: str = None):
    recs = recommend_movies(title, genre)
    return {"recommendations": recs}
