from flask import Flask, render_template, request
import pandas as pd
import logging

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        start = int(request.form['start'])
        end = int(request.form['end'])
        df = pd.read_csv("car.csv")
        avg = df[start:end]['selling_price'].mean()
        return render_template("index.html", result=avg)
    return render_template("index.html", result='')


@app.route('/plots')
def plot():
    return render_template("plots.html")


if __name__ == '__main__':
    app.run()
