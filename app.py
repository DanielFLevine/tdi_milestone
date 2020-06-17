from flask import Flask, render_template, request, redirect, url_for
import selection


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ticker = request.form['ticker']
        column = request.form['column']

        script, div = selection.plot(ticker, column)

        return render_template('index.html', div=div, script=script)
    else:
        return render_template('index.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(port=33507)

