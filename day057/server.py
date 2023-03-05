from flask import Flask, render_template
import random
from datetime import date
import requests

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = date.today().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/<name>")
def info_name(name):
    URL_GENDERIZE = "https://api.genderize.io?name=" + name
    URL_AGIFY = "https://api.agify.io?name=" + name
    response_genderize = requests.get(URL_GENDERIZE)
    gender = response_genderize.json()["gender"]
    response_agify = requests.get(URL_AGIFY)
    age = response_agify.json()["age"]
    name_c = response_agify.json()["name"].title()
    
    return render_template("index2.html", gender=gender, age=age, name=name_c)
    

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/8cf99bd42aa8d118ca78"   
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

    
    
if __name__ == "__main__":
    app.run(debug=True)


