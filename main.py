from flask import Flask, render_template, request

app = Flask(__name__)


def count_words(text):
    """Function to count the number of words in a given text."""
    words = text.split()
    return len(words)

@app.route("/", methods=["GET", "POST"])
def index():
    word_count = None
    error = None

    if request.method == "POST":
        text = request.form.get("text")
        if not text.strip():
            error = "Please enter a valid sentence or paragraph."
        else:
            word_count = count_words(text)

    return render_template("index.html", word_count=word_count, error=error)

if __name__ == "__main__":
    app.run(debug=True)

