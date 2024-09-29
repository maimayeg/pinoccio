from flask import Flask, request, jsonify, session, send_from_directory
from flask_cors import CORS
from flask_session import Session
from models import db, Article
from ai_model import PropagandaGenerator
from datetime import datetime
import os

app = Flask(__name__)
CORS(app, supports_credentials=True)

# Secret key for session management
app.config['SECRET_KEY'] = 'xoxoxoxoxox'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fake_news_2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Session(app)
db.init_app(app)
propaganda_generator = PropagandaGenerator()

with app.app_context():
    db.create_all()


def generate_fake_news(prompt, intensity, use_openai=True):
    """
    Generates fake news using the provided prompt, intensity, and model selection.
    """
    # Re-initialize PropagandaGenerator based on user's choice of model
    global propaganda_generator
    propaganda_generator = PropagandaGenerator(use_openai=use_openai)
    
    # Generate the propaganda using the headline and intensity
    propaganda = propaganda_generator.generate_propaganda(prompt, intensity)
    return propaganda




@app.route('/generate', methods=['POST'])
def generate():
    """
    API endpoint to generate fake news. Accepts JSON payload with prompt, intensity, and model choice.
    """
    data = request.get_json()

    prompt = data.get('prompt')
    intensity = data.get('intensity', 'neutral')  # Default intensity is 'neutral'
    use_openai = data.get('use_openai', True)  # Default model is OpenAI

    # Validate if the prompt (headline) is valid
    # if not propaganda_generator.is_valid_input(prompt):
    #     return jsonify({'error': 'Invalid headline. Please provide a valid news-related headline.'}), 400

    # Generate fake news using the specified model and intensity
    generated_text = generate_fake_news(prompt, intensity, use_openai)

    # Save generated article to the database
    new_article = Article(prompt=prompt, generated_text=generated_text)
    db.session.add(new_article)
    db.session.commit()

    # Optionally, write generated text to a file
    file_path = os.path.join('generated_texts', f'article_{new_article.id}.txt')
    os.makedirs('generated_texts', exist_ok=True)  # Ensure directory exists
    with open(file_path, 'w') as file:
        file.write(generated_text)

        # Return the generated text and the file name
        return jsonify({
            'article': generated_text,
            'file': f'article_{new_article.id}.txt'
        }), 200

@app.route('/deconstruct', methods=['POST'])
def deconstruct():
    """
    API endpoint to deconstruct generated propaganda and return a disclaimer.
    """
    data = request.get_json()
    generated_text = data['generated_text']  # Access generated text from request

    # Deconstruct the article using the global PropagandaGenerator instance
    deconstruction_report = propaganda_generator.deconstruct()

    return jsonify({'deconstruction_report': deconstruction_report}), 200

@app.route('/articles', methods=['GET'])
def get_articles():
    """
    API endpoint to retrieve all generated articles from the database.
    """
    articles = Article.query.all()
    return jsonify([{
        'id': article.id,
        'prompt': article.prompt,
        'generated_text': article.generated_text,
        'timestamp': article.timestamp
    } for article in articles]), 200


if __name__ == '__main__':
    app.run(debug=True)
    


