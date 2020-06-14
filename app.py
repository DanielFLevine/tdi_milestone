from flask import Flask, render_template, request, redirect, url_for
import selection


app = Flask(__name__)


@app.route('/plot/<ticker>/<column>')
def plot(ticker, column):
    script, div = selection.plot(ticker, column)

    return render_template('index.html', div=div, script=script)


@app.route('/', methods=['POST'])
def index():
    ticker = request.form(['ticker'])
    column = request.form(['column'])

    return redirect(url_for('plot', ticker=ticker, column=column))


if __name__ == '__main__':
    app.run(port=33507)

