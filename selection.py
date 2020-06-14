import requests
import pandas as pd
from bokeh.plotting import figure
from bokeh.embed import components
from get_all_tickers import get_tickers as gt

list_of_tickers = gt.get_tickers()


def df(ticker):
    if ticker in list_of_tickers
        data = requests.get(
            r'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + ticker + '&interval=60min&outputsize=full&apikey=9QO32QU9D5ADYS17')

        data = data.json()
        df = pd.DataFrame.from_dict(data["Time Series (60min)"], orient='index')
        df.columns = ['open', 'high', 'low', 'close', 'volume']
        df.index = range(len(df))

        for j in list(df.columns):
            df[j] = df[j].astype('float')
        df['return percent'] = (df['close'] - df['open']) / df['open']

        return df

def plot(ticker,column):
    df = df(ticker)
    if column in df.columns:
        p = figure(plot_height=400, plot_width=1000)
        p.line(x=df.index, y=df[column])

        script, div = components(p)

        return script, div