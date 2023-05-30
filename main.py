#imports

from flask import Flask, render_template, request, redirect

import requests

#create "Flask"

app = Flask(__name__)



@app.route('/')
def home():
    return render_template("homepage.html")
@app.route("/test", methods=['POST'])
def encryptionCC():
    if request.method == 'POST':
        form = request.form
        def encryptionCC1():
            result = "Hello"
            return result
        result1=encryptionCC1()
        return render_template("homepage.html", display = result1)
    return redirect("/homepage")
#run file
if __name__ == "__main__":
    app.run(debug = True)
