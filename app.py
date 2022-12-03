from flask import Flask, render_template
from newsapi import NewsApiClient
import random

app = Flask(__name__)

@app.route("/")
def index():
    # Initialize the news API client
    newsapi = NewsApiClient(api_key="ccfbae83967943ac8f540f90f80e8e56")

    # Fetch the latest headlines from multiple news sources
    headlines = newsapi.get_top_headlines(sources="bbc-news")

    # Select a random headline from the list of headlines
    headline = random.choice(headlines['articles'])

    # Pass the headlines and selected headline to the template for rendering
    return render_template("index.html", headlines=headlines, headline=headline)


if __name__ == "__main__":
    # Set the host and port to allow external access
    app.run(host="0.0.0.0", port=5000)

