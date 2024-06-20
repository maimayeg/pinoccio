import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [prompt, setPrompt] = useState('');
  const [intensity, setIntensity] = useState(5);
  const [article, setArticle] = useState('');
  const [articles, setArticles] = useState([]);
  const [filename, setFilename] = useState('');

  const generateArticle = async () => {
    const response = await axios.post('http://127.0.0.1:5000/generate', {
      prompt,
      intensity,
    });
    setArticle(response.data.article);
    setFilename(response.data.file);
    fetchArticles();
  };

  const fetchArticles = async () => {
    const response = await axios.get('http://127.0.0.1:5000/articles');
    setArticles(response.data);
  };

  useEffect(() => {
    fetchArticles();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Fake News Generator</h1>
      </header>
      <main>
        <div className="input-section">
          <textarea
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder="Enter your prompt here..."
          ></textarea>
          <div className="intensity-controls">
            <label htmlFor="intensity">Intensity:</label>
            <input
              type="range"
              id="intensity"
              min="1"
              max="10"
              value={intensity}
              onChange={(e) => setIntensity(e.target.value)}
            />
          </div>
          <button className="generate-button" onClick={generateArticle}>
            Generate
          </button>
        </div>
        <div className="output-section">
          <h2>Generated Article</h2>
          <p>{article}</p>
          {filename && (
            <a href={`http://127.0.0.1:5000/download/${filename}`} download>
              Download Generated Article
            </a>
          )}
        </div>
        <div className="history-section">
          <h2>Generated Articles History</h2>
          {articles.map((art) => (
            <div key={art.id} className="article-item">
              <p><strong>Prompt:</strong> {art.prompt}</p>
              <p><strong>Intensity:</strong> {art.intensity}</p>
              <p><strong>Article:</strong> {art.generated_text}</p>
              <p><strong>Timestamp:</strong> {new Date(art.timestamp).toLocaleString()}</p>
            </div>
          ))}
        </div>
      </main>
    </div>
  );
}

export default App;
