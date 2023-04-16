from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

# app = Flask(__name__)

app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')


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
    response = {'polarity': polarity, 'subjectivity': subjectivity}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
