from flask import Flask, render_template, request
import requests
import smtplib
import pandas as pd 

app = Flask(__name__)

df = pd.read_csv("C:/Users/T-Gamer/Documents/data/data.txt", )
my_email = list(df["username"])[0]
target_email = list(df["target_email"])[0]
password_gm = list(df["password_gm"])[0]


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


@app.route("/form-entry", methods=["POST"])
def receive_data():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone_number = request.form["phone_number"]
        message = request.form["message"]
        
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password_gm)
            connection.sendmail(from_addr=my_email,
                                to_addrs=target_email,
                                msg=f"\n\nName: {name}\n\nEmail: {email}\n\nPhone number: {phone_number}\n\nMessage: {message}")
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)
    

if __name__ == "__main__":
    app.run(debug=True)

