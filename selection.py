import requests
import pandas as pd
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import Range1d


def ticker_data(ticker):
    data = requests.get(
        r'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=' + ticker + '&outputsize=full&apikey=9QO32QU9D5ADYS17')

    data = data.json()
    df = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient='index')
    df.columns = ['open', 'high', 'low', 'close', 'adjusted close', 'volume', 'dividend count', 'split coefficient']
    df['datetime'] = df.index.astype('datetime64[ns]')
    df.index = range(len(df))

    for j in list(df.columns):
        if j != 'datetime':
            df[j] = df[j].astype('float')
    df = df[::-1]
    df.index = range(len(df))

    return df


def plot(ticker, column):
    df = ticker_data(ticker)
    if column in df.columns:
        p = figure(title=ticker.upper() + " " + column.upper(), plot_height=400, plot_width=1000, x_range=Range1d(0, len(df), bounds="auto"))
        p.title.align = "center"
        p.title.text_font_size = "30px"
        p.xaxis.axis_label = 'Date'
        if column == 'close':
            p.yaxis.axis_label = 'Closing Price'
        elif column == 'open':
            p.yaxis.axis_label = 'Opening Price'
        elif column == 'adjusted close':
            p.yaxis.axis_label = 'Closing Price (Adjusted)'
        elif column == 'high':
            p.yaxis.axis_label = 'High'
        elif column == 'low':
            p.yaxis.axis_label = 'Low'
        p.line(x=df.index, y=df[column])
        p.xaxis.minor_tick_line_color = None
        p.xaxis.major_label_overrides = {i: df['datetime'].iloc[i].strftime('%b %d %Y') for i in
                                         range(len(df))}

        script, div = components(p)

        return script, div
