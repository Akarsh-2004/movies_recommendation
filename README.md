# 🎬 Movie Recommender

A simple React-based movie recommendation app that suggests similar movies based on a given title or genre.

## 🌐 Live Demo
👉 [moviesideas.netlify.app](https://moviesideas.netlify.app)

## 📦 Features
- 🔍 Search by movie title or genre
- 🤖 Fetches similar recommendations from a hosted ML API
- ⚡ Fast and minimal UI using React + Fetch API

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/Akarsh-2004/movies_recommendation.git
cd movies_recommendation/client
```

### 2. Install dependencies
```bash
npm install
```

### 3. Run the app locally
```bash
npm run dev
```

**Backend is live at:** https://movies-idea.onrender.com

## 📡 Backend API

The frontend sends requests to:
```bash
GET /recommend/?title=your_input
```

**Example:**
```
https://movies-idea.onrender.com/recommend/?title=inception
```

## 📝 Note
You can enter either a movie title or a genre (like "action", "comedy", etc.) to get relevant movie recommendations.
