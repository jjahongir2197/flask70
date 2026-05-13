from flask import Flask, render_template

app = Flask(__name__)

stats = {
    "users": 120,
    "posts": 45,
    "comments": 300
}

@app.route("/")
def dashboard():

    return render_template("index.html", stats=stats)

if __name__ == "__main__":
    app.run(debug=True)
