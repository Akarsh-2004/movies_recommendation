from fastapi import FastAPI, Query
from movies_recommender import recommend_movies
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "https://moviesideas.netlify.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
def ping():
    return {"message": "pong"}
    

@app.get("/recommend/")
def recommend(title: str = None, genre: str = None):
    recs = recommend_movies(title, genre)
    return {"recommendations": recs}
