import firebase_admin
from flask import Flask, render_template
from random import randint
from datetime import datetime
import firebase_admin
from firebase_admin import firestore, credentials
import requests

app = Flask(__name__)

cred = credentials.Certificate('blog-website-60fe4-3656d826f1fc.json')
firebase_app = firebase_admin.initialize_app(cred)
db = firestore.client()
blogs = db.collection("blogs").stream()
data = []
for doc in blogs:
    data.append(doc.to_dict())


@app.route("/")
def home():
    number = randint(1, 200)
    current_year = datetime.now().year
    return render_template("index.html",blogs=data, num=number, curr_year=current_year)


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


@app.route("/post/<post_id>")
def post_page(post_id):
    post_content = None
    for i in data:
        if int(i['id']) == int(post_id):
            post_content = i
    return render_template("post.html", data=post_content)


if __name__ == "__main__":
    app.run(debug=True)