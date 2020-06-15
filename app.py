from flask import Flask, render_template, request, redirect, url_for
import selection


app = Flask(__name__)


@app.route('/<ticker>/<column>', methods=["GET"])
def plot(ticker, column):
    script, div = selection.plot(ticker, column)

    return render_template('index.html', div=div, script=script)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ticker = request.form['ticker']
        column = 'close'

        return redirect(url_for('plot', ticker=ticker, column=column))
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(port=33507)

