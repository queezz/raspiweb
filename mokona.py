"""
Code created by Matt Richardson 
for details, visit:  http://mattrichardson.com/Raspberry-Pi-Flask/inde...
"""
from flask import Flask, render_template
import datetime
import pandas as pd
import os

app = Flask(__name__)


@app.route("/")
def hello():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {"title": "Mokona", "time": timeString, "phrase": choosephrase()}
    return render_template("index.html", **templateData)


def choosephrase():
    bpth = os.path.dirname(os.path.realpath(__file__))
    lines = pd.read_csv(os.path.join(bpth, "phrases.txt"), names=["phrase"])
    return lines.sample().iloc[0][0]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
