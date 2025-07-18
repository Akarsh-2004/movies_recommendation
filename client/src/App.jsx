import { useState } from 'react';
import './App.css';

function App() {
  const [title, setTitle] = useState('');
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    if (!title.trim()) return;
    setLoading(true);
    try {
      const res = await fetch(`http://127.0.0.1:8000/recommend/?title=${encodeURIComponent(title)}`);
      const data = await res.json();
      setRecommendations(data.recommendations || []);
    } catch (error) {
      console.error('Error fetching recommendations:', error);
      setRecommendations([]);
    }
    setLoading(false);
  };

  return (
    <div className="app">
      <h1>Movie Recommender</h1>
      <input
        type="text"
        value={title}
        placeholder="Enter movie title"
        onChange={(e) => setTitle(e.target.value)}
      />
      <button onClick={handleSearch} disabled={loading}>
        {loading ? 'Searching...' : 'Get Recommendations'}
      </button>

      <ul>
        {recommendations.map((rec, index) => (
          <li key={index}>{rec}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
