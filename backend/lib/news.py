import requests
from datetime import datetime, timedelta
from lib.env import env

api_key = env.get("NEWS_API_KEY")

def fetch_news(asset_name):
    try:
        base_url = "https://newsapi.org/v2/everything"
        
        end_date = datetime.now()
        start_date = end_date - timedelta(days=14)
        
        params = {
            'apiKey': api_key,
            'q': asset_name,
            'from': start_date.strftime('%Y-%m-%d'),
            'to': end_date.strftime('%Y-%m-%d'),
            'language': 'en',
            'sortBy': 'relevancy',
            'pageSize': '20'
        }
        
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        data = response.json()
        news = []

        if data['totalResults'] == 0:
            return ''
                
        for article in data['articles']:
            title = article['title']
            description = article['description']
            content = article['content']
            url = article['url']
            news.append(f'title: {title}, description: {description}, content: {content}, url: {url}')

        return ' '.join(news)
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return ''
