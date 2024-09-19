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


def generate_fake_news(prompt):
   
    
    propaganda = propaganda_generator.generate_propaganda(prompt)
    return propaganda




@app.route('/generate', methods=['POST'])
def generate():
    

    data = request.get_json()
    prompt = data['prompt']

    generated_text = generate_fake_news(prompt)

    new_article = Article(prompt=prompt, generated_text=generated_text)
    db.session.add(new_article)
    db.session.commit()

    file_path = os.path.join('generated_texts', f'article_{new_article.id}.txt')
    with open(file_path, 'w') as file:
        file.write(generated_text)

    

    return jsonify({
        'article': generated_text,
        'file': f'article_{new_article.id}.txt'
    }), 200

@app.route('/deconstruct', methods=['POST'])
def deconstruct():
    """
    Takes the generated text from the request body and analyzes it using the 
    global propaganda_generator instance. Returns the deconstruction report.
    """

    data = request.get_json()
    generated_text = data['generated_text']  # Access generated text from request

    # Analyze the generated text
    deconstruction_report = propaganda_generator.deconstruct()

    return jsonify({'deconstruction_report': deconstruction_report}), 200
    
@app.route('/articles', methods=['GET'])
def get_articles():
    
    articles = Article.query.all()
    return jsonify([{
        'id': article.id,
        'prompt': article.prompt,
        'generated_text': article.generated_text,
        'timestamp': article.timestamp
    } for article in articles]), 200
    




if __name__ == '__main__':
    app.run(debug=True)

