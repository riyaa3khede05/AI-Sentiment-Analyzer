from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis")

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        text = request.form["text"]

        prediction = sentiment_pipeline(text)

        result = prediction[0]['label']

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)