from flask import Flask, render_template, request, redirect, send_file

app = Flask("Devjob_main")

@app.route("/")
def home():
    return render_template("main.html")


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)