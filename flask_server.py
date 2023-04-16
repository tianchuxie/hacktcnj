from flask import Flask, render_template, request, jsonify
from textblob import TextBlob
import spacy

# app = Flask(__name__)

app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')

nlp = spacy.load('en_core_web_sm')


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/make')
def makeQubit():
    return render_template('qubit.html')

@app.route('/quture')
def quture():
    return render_template('quture.html')

@app.route('/analyze', methods=['POST'])
def analyze_text():
    text = request.form['text']
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    doc = nlp(text)
    results = {
        'input_sentence': text,
        'tokens': [token.text for token in doc],
        'pos_tags': [token.pos_ for token in doc],
        'ner_tags': [token.ent_type_ for token in doc],
        # Add more analysis results here
    }
    response = {'polarity': polarity, 'subjectivity': subjectivity, 'results': results}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
