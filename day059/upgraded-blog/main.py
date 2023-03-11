from flask import Flask, render_template
import requests

app = Flask(__name__)



@app.route("/")
def home():
    url = "https://api.npoint.io/2900b775473888821081"
    response = requests.get(url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post/<id>")
def post(id):
    url = "https://api.npoint.io/2900b775473888821081"
    response = requests.get(url)
    all_posts = response.json()
    post_content = all_posts[int(id) - 1]
    return render_template("post.html", post=post_content)

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)

