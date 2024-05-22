from flask import Flask, render_template, request, send_file
from main import TextToSpeech

app = Flask(__name__)
text_to_speech = TextToSpeech()


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.form
        text_to_speech.run(data["message"])
        return render_template("index.html")
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port=8000)
