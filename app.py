import os
import csv
import talib
import yfinance as yf
import pandas
from flask import Flask, escape, request, render_template, redirect, url_for
from patterns import candlestick_patterns
from companies import company_name
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/screener')
def screener():
    pattern = request.args.get('pattern', False)
    if pattern:
        print(pattern)
    stocks = {}

    with open('datasets/symbols.csv') as f:
        for row in csv.reader(f):
            stocks[row[0]] = {'company': row[1]}

    if pattern:
        for filename in os.listdir('datasets/daily'):
            df = pandas.read_csv('datasets/daily/{}'.format(filename))
            pattern_function = getattr(talib, pattern)
            symbol = filename.split('.')[0]

            try:
                results = pattern_function(
                    df['Open'], df['High'], df['Low'], df['Close'])
                last = results.tail(1).values[0]

                if last > 0:
                    stocks[symbol][pattern] = 'bullish'
                elif last < 0:
                    stocks[symbol][pattern] = 'bearish'
                else:
                    stocks[symbol][pattern] = None
            except Exception as e:
                print('failed on filename: ', filename)

    return render_template('screener.html', candlestick_patterns=candlestick_patterns, stocks=stocks, pattern=pattern)


@app.route('/refresh')
def refresh():
    return render_template('refresh.html')


@app.route('/download_Data', methods=['POST'])
def download_Data():
    # Download the dataset
    """
    with open('datasets/symbols.csv') as f:
        for line in f:
            if "," not in line:
                continue
            symbol = line.split(",")[0]
            data = yf.download(symbol, start="2022-01-01",
                               end=datetime.date.today())
            data.to_csv('datasets/daily/{}.csv'.format(symbol))
    """

    print("\nEXECUTION COMPLETED")
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
