# app.py
from flask import Flask, render_template, request
from youtube_utils import extract_video_id, get_comments
from sentiment_analysis import analyze_sentiments

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    error = None

    if request.method == "POST":
        url = request.form.get("url")
        video_id = extract_video_id(url)

        if not video_id:
            error = "Invalid YouTube URL"
        else:
            try:
                comments = get_comments(video_id, max_comments=50)
                results = analyze_sentiments(comments)
            except Exception as e:
                error = f"Error: {e}"

    return render_template("index.html", results=results, error=error)

if __name__ == "__main__":
    app.run(debug=True)
