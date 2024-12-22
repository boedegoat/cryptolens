from pydantic import BaseModel
import requests
from lib.env import env
from tradingview_ta import TA_Handler, Interval
from lib.ai import get_ai_completions
import json

api_key = env.get("ALPHA_VANTAGE_API_KEY")

class SymbolSearchResult(BaseModel):
    symbol: str
    screener: str
    exchange: str

def symbol_search(query):
    prompt = f"""I'm using tradingview_ta python library.
For the search term '{query}', please provide the correct trading symbol, screener, and exchange.
The format should match the TA_Handler parameters:
- symbol: trading symbol
- screener: 'america', 'indonesia', 'crypto', etc
- exchange: 'NASDAQ', 'BINANCE', etc

Please return the response in this JSON format:
{{
    "symbol": "TSLA",
    "screener": "america",
    "exchange": "NASDAQ"
}}"""
    
    return json.loads(get_ai_completions(
        model='gpt-4o',
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.0,
        response_format={"type": "json_object"}
    ))

def fetch_technical_analysis(symbol, screener, exchange):
    try:
        result = TA_Handler(
            symbol=symbol,
            screener=screener,
            exchange=exchange,
            interval=Interval.INTERVAL_1_DAY
        )
        
        analysis = result.get_analysis()
        return analysis

    except Exception as e:
        raise RuntimeError(f"Failed to fetch technical analysis: {str(e)}")

def fetch_prices(symbol):
    base_url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": api_key,
        "outputsize": "compact" 
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        # Extract time series data
        time_series = data.get("Time Series (Daily)", {})
        
        # Convert to more convenient format
        prices = {
            date: {
                'open': float(values['1. open']),
                'high': float(values['2. high']),
                'low': float(values['3. low']),
                'close': float(values['4. close']),
                'volume': int(values['5. volume'])
            }
            for date, values in time_series.items()
        }

        return "\n".join([f"- {key}: {value}" for key, value in prices.items()])

    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Failed to fetch data: {str(e)}")