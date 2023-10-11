from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
    return render_template("login.html")

app.run()