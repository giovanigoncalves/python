from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
import pandas as pd 
from pprint import pprint

data = pd.read_csv("C:/Users/T-Gamer/Documents/data/data.txt")

USERNAME = data["login_movie"]
API = data["MOVIE_API"]
TOKEN = str(data["MOVIE_TOKEN"][0])
MOVIE_URL = "https://image.tmdb.org/t/p/w500/"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
# print(TOKEN)


headers = {
    "accept": "application/json",
    "Authorization": "Bearer " + TOKEN
}

    

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(500), nullable=True)
    img_url = db.Column(db.Text, nullable=False)


class RateMovieForm(FlaskForm):
    rating = FloatField("Your rating out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review")
    submit = SubmitField("Submit")


class FindMovieForm(FlaskForm):
    title = StringField("Movie Title")
    submit = SubmitField("Add Movie")




@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        print(movie.rating)
        movie.review = form.review.data
        print(movie.review)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form, movie=movie)
    

@app.route("/delete", methods=["GET", "POST"])
def delete():
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    del movie
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = FindMovieForm()
    
    movie = Movie()
    if form.validate_on_submit():
        movie_title = form.title.data
        
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": API, "query": movie_title})
        result = response.json()["results"]
        return render_template("select.html", options=result)
    return render_template("add.html", form=form)


@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key":API, "language":"en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("rate_movie", id=new_movie.id))

    
if __name__ == '__main__':
    app.run(debug=True)
