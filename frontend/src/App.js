import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [prompt, setPrompt] = useState('');
  const [article, setArticle] = useState('');
  const [deconstructionReport, setDeconstructionReport] = useState(null);
  const [articles, setArticles] = useState([]);
  const [filename, setFilename] = useState('');

  // New state variables for intensity and model choice
  const [intensity, setIntensity] = useState('neutral'); // Default intensity is 'neutral'
  const [useOpenAI, setUseOpenAI] = useState(true); // Default model is OpenAI (true)

  // Function to generate an article with selected intensity and model
  const generateArticle = async () => {
    const response = await axios.post('http://127.0.0.1:5000/generate', {
      prompt,
      intensity,  // Pass the selected intensity to the backend
      use_openai: useOpenAI // Pass the model choice to the backend
    });
    setDeconstructionReport(null);  // Clear deconstruction report on new article generation
    setArticle(response.data.article);  // Set the generated article
    setFilename(response.data.file);    // Set the filename of the generated article
    fetchArticles();  // Fetch all articles from the database
  };

  // Function to fetch all articles
  const fetchArticles = async () => {
    const response = await axios.get('http://127.0.0.1:5000/articles');
    setArticles(response.data);  // Update articles list
  };
  
  // Function to deconstruct the generated article
  const deconstructArticle = async () => {
    if (!article) return; // Check if an article exists before deconstruction

    const response = await axios.post('http://127.0.0.1:5000/deconstruct', {
      generated_text: article,  // Pass the generated article text for deconstruction
    });
    setDeconstructionReport(response.data.deconstruction_report);  // Set deconstruction report
  };

  // Fetch all articles on initial load
  useEffect(() => {
    fetchArticles();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Pinocchio</h1>
      </header>
      <main>
        <div className="input-section">
          <textarea
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder="Enter an article or headline here to manipulate..."
          ></textarea>
          
          {/* Flex container for dropdown and radio buttons */}
          <div className="controls-container">
            {/* Dropdown for selecting intensity */}
            <div className="intensity-select">
              <label htmlFor="intensity">Select Intensity:</label>
              <select
                id="intensity"
                value={intensity}
                onChange={(e) => setIntensity(e.target.value)}
              >
                <option value="neutral">Neutral</option>
                <option value="intense">Intense</option>
                <option value="very dramatic">Very Dramatic</option>
              </select>
            </div>

            {/* Radio buttons for selecting the model */}
            <div className="model-select">
              <label>Select Model:</label>
              <div>
                <input
                  type="radio"
                  id="openai"
                  name="model"
                  value="openai"
                  checked={useOpenAI}
                  onChange={() => setUseOpenAI(true)}
                />
                <label htmlFor="openai">OpenAI GPT</label>
              </div>
              <div>
                <input
                  type="radio"
                  id="llama"
                  name="model"
                  value="llama"
                  checked={!useOpenAI}
                  onChange={() => setUseOpenAI(false)}
                />
                <label htmlFor="llama">LLaMA</label>
              </div>
            </div>
          </div>

          {/* Button container */}
          <div className="button-container">
            <button className="generate-button" onClick={generateArticle}>
              Generate
            </button>

            <button className="deconstruct-button" onClick={deconstructArticle}>
              Deconstruct
            </button>
          </div>
        </div>

        {/* Flex container for output sections */}
        <div className="output-container">
          {/* Section to display the generated article */}
          <div className="output-section">
            <h2>Generated Article</h2>
            <p>{article}</p>
          </div>
          
          {/* Display the deconstruction report if available */}
          {deconstructionReport && (
            <div className="deconstruction-report">
              <h2>Deconstruction Report</h2>
              <p>{deconstructionReport}</p>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}

export default App;
