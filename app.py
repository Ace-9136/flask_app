import os
import csv
import talib
import yfinance as yf
import pandas
from flask import Flask, request, render_template, jsonify
from patterns import candlestick_patterns
from companies import company_name
import datetime
import time
import threading

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
            var = filename.split('.')[0]
            symbol = var+".NS"

            try:
                results = pattern_function(
                    df['Open'], df['High'], df['Low'], df['Close'])
                last = results.tail(10).values[0]
                """
                if last != 0:
                    print(filename)
"""
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
def refreshData():
    # code to refresh the dataset goes here
    
    return jsonify({'status': 'success'})


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/execute_function')
def execute_function():
    # Execute your Python function here
    with open('datasets/symbols.csv') as f:
        for line in f:
            if "," not in line:
                continue
            symbol = line.split(",")[0]
            data = yf.download(symbol, start="2022-01-01",
                               end=datetime.date.today())
            data.to_csv('datasets/daily/{}.csv'.format(symbol))
    # return the refreshed data in JSON format
    result = "Function executed successfully"
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
