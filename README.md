# Stock Sensei
This is a Flask application that allows users to perform two main functions related to stock analysis: plotting candlestick graphs and finding patterns in a list of stocks. This application has not been deployed yet and can be run locally on your machine.
## Features
The Flask Stock Analysis Application provides the following features:

1. Candlestick Graph Plotting: Users can visualize the historical price data of a stock using candlestick graphs. Candlestick graphs provide information about the      opening, closing, highest, and lowest prices for a given time period.

2. Pattern Detection: Users can input a list of stocks, and the application will analyze the data to detect any patterns. These patterns could include trends,          reversals, or specific chart patterns like head and shoulders, double tops, etc.

## Installation
To run the Flask Stock Analysis Application locally, follow the steps below:/

1. Clone the repository:
    ```bash
    git clone https://github.com/Ace-9136/flask_app
    
2. Change to the project directory:
    ```bash
    cd flask-app

3. Set up a virtual environment (recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

5. Start the Flask application:
    ```bash
    python app.py

6. Open your browser and navigate to http://localhost:5000 to access the application.
## Usage
Once you have the Flask application running, you can access the following endpoints:

* Candlestick Graph Plotting: To plot a candlestick graph, navigate to http://localhost:5000/ in your browser. Enter the necessary information, such as the stock symbol, time period, and any additional parameters required. Click on the "Plot" button to visualize the candlestick graph.

* Pattern Detection: To find patterns in a list of stocks, go to http://localhost:5000/screener in your browser. Input the list of stock symbols or upload a CSV file containing the stock data. Click on the "Find Patterns" button to perform the analysis and display any detected patterns.
## Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, please submit an issue or a pull request.

## License
This project is licensed under the MIT License.
