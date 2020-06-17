import requests
import pandas as pd
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import Range1d


def ticker_data(ticker):
    data = requests.get(
        r'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + ticker + '&interval=60min&outputsize=full&apikey=9QO32QU9D5ADYS17')

    data = data.json()
    df = pd.DataFrame.from_dict(data["Time Series (60min)"], orient='index')
    df.columns = ['open', 'high', 'low', 'close', 'volume']
    df['datetime'] = df.index.astype('datetime64[ns]')
    df.index = range(len(df))

    for j in list(df.columns):
        if j != 'datetime':
            df[j] = df[j].astype('float')
    df['return_percent'] = (df['close'] - df['open']) / df['open']

    df = df[::-1]
    df.index = range(len(df))

    return df


def plot(ticker, column):
    df = ticker_data(ticker)
    if column in df.columns:
        p = figure(title=ticker, plot_height=400, plot_width=1000, x_range=Range1d(0, len(df), bounds="auto"))
        p.title.align = "center"
        p.title.text_font_size = "25px"
        p.line(x=df.index, y=df[column])
        p.xaxis.minor_tick_line_color = None
        p.xaxis.major_label_overrides = {i: df['datetime'].iloc[i].strftime('%b %d %I:%M%p') for i in
                                         range(len(df))}

        script, div = components(p)

        return script, div
