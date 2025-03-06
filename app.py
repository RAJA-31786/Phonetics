from flask import Flask, render_template, request
import subprocess
from phonetic_transcription import transcribe_word
from featuretable import features

app = Flask(__name__)


# Home page with a form to enter words
@app.route('/')
def index():
    return render_template('index.html')


# Handle form submission and run transcription + metrics
@app.route('/transcribe', methods=['POST'])
def transcribe():
    word = request.form['word']
    transcription = transcribe_word(word)

    # Save transcription to file for metrics
    with open("transcription_output.txt", "w") as file:
        file.write(f"{word}:{transcription}:{transcription}\n")

    # Run performance_metrics.py and capture output
    result = subprocess.run(["python", "performance_metrics.py"], capture_output=True, text=True)
    metrics = result.stdout

    return render_template('result.html', word=word, transcription=transcription, metrics=metrics)


if __name__ == "__main__":
    app.run(debug=True)
