from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure
from bokeh.embed import components
import requests
import pandas as pd


app = Flask(__name__)

@app.route('/')
def index():
    data_nvda = requests.get(
        r'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=NVDA&interval=60min&outputsize=full&apikey=9QO32QU9D5ADYS17')
    data_amd = requests.get(
        r'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AMD&interval=60min&outputsize=full&apikey=9QO32QU9D5ADYS17')

    data_nvda = data_nvda.json()
    data_amd = data_amd.json()

    df_nvda = pd.DataFrame.from_dict(data_nvda["Time Series (60min)"], orient='index')
    df_amd = pd.DataFrame.from_dict(data_amd["Time Series (60min)"], orient='index')

    df_nvda['datetime'] = df_nvda.index.astype('datetime64[ns]')
    df_amd['datetime'] = df_amd.index.astype('datetime64[ns]')
    df_nvda.columns = ['open', 'high', 'low', 'close', 'volume', 'datetime']
    df_amd.columns = ['open', 'high', 'low', 'close', 'volume', 'datetime']

    df_nvda.index = range(len(df_nvda))
    df_amd.index = range(len(df_nvda))

    a = [df_nvda, df_amd]
    for i in a:
        for j in list(i.columns):
            if j != 'datetime':
                i[j] = i[j].astype('float')
        i['return percent'] = (i['close'] - i['open']) / i['open']

    p = figure(plot_height=400, plot_width=1000)
    r_nvda = p.line(x=df_amd.index, y=df_nvda['return percent'])
    r_amd = p.line(x=df_amd.index, y=df_amd['return percent'], color='green')

    script, div = components(p)

    return render_template('index.html', div=div, script=script)

if __name__ == '__main__':
    app.run(port=33507)

