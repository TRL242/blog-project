from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    blog_response = requests.get(blog_url)
    blog_data = blog_response.json()

    return render_template("index.html", posts=blog_data)

@app.route('/post/<id>')
def blog_post():
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    blog_response = requests.get(blog_url)
    blog_data = blog_response.json()

    return render_template("index.html", posts=blog_data)

if __name__ == "__main__":
    app.run(debug=True)
