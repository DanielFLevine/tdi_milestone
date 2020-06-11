from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure
from bokeh.embed import components

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(port=33507)


@app.route('/dashboard/')
def show_dashboard():
    plot = figure(plot_height=300, sizing_mode='scale_width')

    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = [2**v for v in x]

    plot.line(x, y, line_width=4)

    script, div = components(plot)

    return render_template('layout.html', div=div, script=script)

