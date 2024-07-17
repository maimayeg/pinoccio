
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [prompt, setPrompt] = useState('');
  const [article, setArticle] = useState('');
  const [deconstructionReport, setDeconstructionReport] = useState(null);

  const [articles, setArticles] = useState([]);
  const [filename, setFilename] = useState('');

  const generateArticle = async () => {
    const response = await axios.post('http://127.0.0.1:5000/generate', {
      prompt,
    });
    setDeconstructionReport(null);
    setArticle(response.data.article);
    setFilename(response.data.file);
    fetchArticles();
  };

  const fetchArticles = async () => {
    const response = await axios.get('http://127.0.0.1:5000/articles');
    setArticles(response.data);
  };
  
  const deconstructArticle = async () => {
    if (!article) return; // Check if article exists before deconstruction

    const response = await axios.post('http://127.0.0.1:5000/deconstruct', {
      generated_text: article,
    });
    setDeconstructionReport(response.data);
  }

  useEffect(() => {
    fetchArticles();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Pinnoccio</h1>
      </header>
      <main>
        <div className="input-section">
          <textarea
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder="Enter an article or headline here to manipulate..."
          ></textarea>
          
          <button className="generate-button" onClick={generateArticle}>
            Generate
          </button>
          <button className="deconstruct-button" onClick={deconstructArticle}>
              Deconstruct
            </button>
        </div>
        <div className="output-section">
          <h2>Generated Article</h2>
          <p>{article}</p>
          
        </div>
        
      </main>
    </div>
  );
}

export default App;

