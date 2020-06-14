from flask import Flask, render_template, request, redirect
import selection


app = Flask(__name__)


@app.route('/')
def index():
    script, div = selection.plot('NVDA', 'close')

    return render_template('index.html', div=div, script=script)


if __name__ == '__main__':
    app.run(port=33507)

