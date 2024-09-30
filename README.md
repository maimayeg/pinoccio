# Pinocchio: Fake News Generator

Pinocchio is a web application that generates propaganda articles based on provided headlines using either OpenAI's GPT models or the LLaMA model. This app also deconstructs generated articles by providing a disclaimer.

## Table of Contents

- [Demo](#demo)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [Contact](#contact)


## Demo

Below is a screenshot of the Pinocchio Fake News Generator in action:

![Pinocchio Demo](pinoccio.png)

## Features
- Generate fake news articles with selectable intensity levels.
- Choose between different AI models (OpenAI's GPT or LLaMA).
- Deconstruct articles to include disclaimers.

## Technology Stack
- **Frontend**: React.js
- **Backend**: Flask (Python)
- **Database**: SQLite
- **AI Models**: OpenAI GPT & LLaMA
- **Styling**: Custom CSS
## Getting Started

### Prerequisites

- Python 3.8+
- Node.js & npm
- Flask
- OpenAI API Key
### Installation

Follow these steps to set up the project on your local machine.

### Backend Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/maimayeg/pinocchio.git
   cd pinocchio
   ```
2. Navigate to the backend folder
3. **Install Python dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set your OpenAI API Key**:
   In `key.py`, update your API key.
5. **Run the Flask app**:
    ```bash
   python3 app.py
   ```
### Frontend Setup
1. **Navigate to the frontend directory**: 
 ```bash
   cd frontend
   ```
2. **Install frontend dependencies**: 
```bash
npm install
```
3. **Start the React app**:

```bash

npm start
```
## Usage

Once both the frontend and backend are running:

1. Open your browser and navigate to `http://localhost:3000`.
2. Enter a headline or article into the input field.
3. Choose the intensity level and the AI model (OpenAI GPT or LLaMA).
4. Click "Generate" to generate an article.
5. Optionally, click "Deconstruct" to reveal the disclaimer.

## API Endpoints

### `/generate` (POST)

- Generates a fake news article.
- **Input**: JSON with `prompt`, `intensity`, and `use_openai`.
- **Output**: Generated article and file name.

### `/deconstruct` (POST)

- Deconstructs the generated article to provide a disclaimer.

### 11. **Contributing**
- Guidelines for contributing to the project, including how to fork, clone, and create a pull request.

Example:
```markdown

## Contributing

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m 'Add some AmazingFeature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a pull request.
## Contact

For any inquiries or support, contact [mai mayeg, Myrto Sideri](mailto:abdelaal@uni-potsdam.de,  sideri.myrto@uni-potsdam.de).

