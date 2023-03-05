from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    text_url = "https://api.npoint.io/a681c7fcf0427acc0127"
    response = requests.get(text_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:id>')
def show_text(id):
    text_url = "https://api.npoint.io/a681c7fcf0427acc0127"
    response = requests.get(text_url)
    all_posts = response.json()
    post = all_posts[id - 1]
    return render_template("post.html", post=post)
    

if __name__ == "__main__":
    app.run(debug=True)



# text_url = "https://api.npoint.io/a681c7fcf0427acc0127"
# response = requests.get(text_url)
# posts = response.json()
# pprint(posts[0]["body"])