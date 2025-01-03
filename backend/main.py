import threading
import firebase_admin
from firebase_admin import credentials, firestore
from icecream import ic
from lib.reddit import *
from lib.technical_data import *
from lib.news import *
from crewai import Agent, Task, Crew, Process, LLM
from datetime import datetime
from pathlib import Path
import os
import uuid

# Initialize Firebase
cred = credentials.Certificate('firebase_config.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def analyze_crypto_asset(input_asset):
    analyze_id = uuid.uuid4()
    
    def update_status(task_name, status, details=None, is_all_completed=False):
        doc_ref = db.collection('crypto_analysis').document(f'{input_asset}_{analyze_id}')
        doc_ref.set({
            'task_name': task_name,
            'status': status,
            'details': details,
            'is_all_completed': is_all_completed,
            'timestamp': datetime.now().isoformat()
        }, merge=True)
    
    def run_analysis():
        try:
            # asset symbol search
            update_status('Searching Symbol', 'processing')
            symbol_search_result = symbol_search(input_asset)
            ic(symbol_search_result)
            update_status('Searching Symbol', 'completed', symbol_search_result)

            symbol = symbol_search_result['symbol']
            exchange = symbol_search_result['exchange']
            screener = symbol_search_result['screener']

            # fetch prices
            update_status('Fetching Prices', 'processing')
            price_history = fetch_prices(symbol)
            ic(price_history)
            update_status('Fetching Prices', 'completed', price_history)

            # fetch technical analysis
            update_status('Fetching Technical Analysis Data', 'processing')
            ta_analysis = fetch_technical_analysis(
                symbol=symbol, 
                screener=screener, 
                exchange=exchange
            )
            ic(ta_analysis.summary)
            ic(ta_analysis.indicators)
            update_status('Fetching Technical Analysis Data', 'completed', {
                'summary': ta_analysis.summary,
                'indicators': ta_analysis.indicators
            })

            # fetch news
            update_status('Fetching News Data', 'processing')
            fetch_news_results = fetch_news(input_asset)
            ic(fetch_news_results)
            update_status('Fetching News Data', 'completed', fetch_news_results)

            # fetch reddit sentiment analysis
            update_status('Generating Subreddits', 'processing')
            generate_subreddits_results = generate_subreddits(input_asset)
            subreddits = generate_subreddits_results['subreddits']
            ic(subreddits)
            update_status('Generating Subreddits', 'completed', subreddits)

            update_status('Fetching Subreddits Data', 'processing')
            fetch_subreddits_results = fetch_subreddits(subreddits, input_asset, update_status)
            ic(fetch_subreddits_results)
            update_status('Fetching Subreddits Data', 'completed', fetch_subreddits_results)

            update_status('Analyzing Final Results', 'processing')

            # Format technical analysis data
            technical_context = f"""
            Technical Analysis Data for {symbol}:

            Price History Data:
            {price_history}

            Summary Analysis:
            - Recommendation: {ta_analysis.summary['RECOMMENDATION']}
            - Buy Signals: {ta_analysis.summary['BUY']}
            - Sell Signals: {ta_analysis.summary['SELL']}
            - Neutral Signals: {ta_analysis.summary['NEUTRAL']}

            Key Technical Indicators:
            """
            # Add formatted indicators
            for indicator_name, value in ta_analysis.indicators.items():
                technical_context += f"- {indicator_name}: {value}\n"

            # Format news data
            news_context = f"""
            News Data for {input_asset}:
            {fetch_news_results}
            """

            # Format reddit data
            reddit_context = f"""
            Reddit Data for {input_asset}:
            Analyzed Subreddits: {','.join(subreddits)}
            Sentiment Data: {fetch_subreddits_results}
            """

            # analyze with ai
            technical_llm = LLM(
                model='gpt-4o',
                temperature=0.1,
                api_key=os.getenv('OPENAI_API_KEY'),
                base_url='https://api.openai.com/v1'
            )

            sentiment_llm = LLM(
                model='gpt-4o',
                temperature=0.25,
                api_key=os.getenv('OPENAI_API_KEY'),
                base_url='https://api.openai.com/v1'
            )

            techninal_analyst = Agent(
                role='Technical Analyst',
                backstory='''A seasoned financial market technical analyst with over 15 years of experience in quantitative analysis and technical trading. 
                Expert in chart patterns, technical indicators, and statistical analysis. Previously worked at top investment banks and hedge funds.
                Known for combining multiple technical analysis methods to provide accurate market predictions.
                Specialized in price action analysis and historical price pattern recognition for determining key levels and trend directions.''',
                goal='''Analyze technical indicators, price patterns, and historical price action to provide highly accurate support/resistance levels, 
                clear directional bias (buy/sell/neutral), and data-driven price predictions. 
                Must provide comprehensive reasoning behind each technical conclusion using both indicator analysis and price action confirmation.''',
                verbose=True,
                llm=technical_llm
            )

            news_analyst = Agent(
                role='News Analyst',
                backstory='''Former financial journalist with 12 years of experience covering global markets and companies.
                Expert in analyzing market-moving news, corporate announcements, and macroeconomic events.
                Skilled at identifying key narrative shifts that impact asset valuations.
                Specializes in separating signal from noise in financial news.''',
                goal='''Analyze news sentiment and important events to determine their impact on the asset's value.
                Identify key narrative trends and potential future catalysts.
                Provide a balanced view of positive and negative news factors.''',
                verbose=True,
                llm=sentiment_llm
            )

            reddit_analyst = Agent(
                role='Reddit Sentiment Analyst',
                backstory='''Social media sentiment expert with expertise in analyzing retail investor behavior and crowd psychology.
                Specialized in filtering quality insights from social media noise.
                Experienced in identifying emerging trends and retail sentiment shifts on investment-focused communities.
                Known for balancing quantitative and qualitative social sentiment analysis.''',
                goal='''Analyze Reddit sentiment to gauge retail investor outlook and identify emerging trends.
                Separate meaningful insights from noise and provide reasoning for sentiment conclusions.
                Identify potential early warning signals from retail sentiment shifts.''',
                verbose=True,
                llm=sentiment_llm
            )

            techninal_analyst_task = Task(
                description=f'''Using the following technical analysis data:
{technical_context}

Conduct a thorough technical analysis by:
1. Analyzing price action and historical price patterns to identify trend direction
2. Identifying key support and resistance levels using price history and multiple timeframes
3. Analyzing all available technical indicators including RSI, MACD, Moving Averages
4. Evaluating current price trends and patterns in relation to historical movements
5. Generating a clear buy/sell/wait recommendation with confidence level
6. Providing a reasonable price prediction range based on historical price action and current indicators
7. Explaining the reasoning behind each conclusion using both price action and technical evidence''',
agent=techninal_analyst,
expected_output='''## 📊 Technical Analysis Report

### 🎯 TL;DR Summary:
🔍 Direction: [🐂 Bullish/🐻 Bearish]
📊 Support: $[price]
📈 Resistance: $[price]
💡 Action: [Buy/Sell/Wait] (Confidence: [X]%)
⚡ Key Points:
- [Quick bullet point 1]
- [Quick bullet point 2]
- [Quick bullet point 3]

### 🎯 Current Trend Analysis:
[Your trend analysis here]

### 📈 Support and Resistance Levels:
[Support and resistance details]

### 💰 Recommendation:
[Your buy/sell/wait recommendation with confidence %]

### 🔮 Price Predictions:
- Short-term (1-7 days): [prediction]
- Medium-term (1-3 months): [prediction]

### 📑 Technical Reasoning:
[Your comprehensive analysis]

### 📉 Key Technical Indicators:
[List key indicators]

### 📋 Historical Patterns:
[Relevant patterns]

### ⚠️ Risk Factors:
[List potential risks]''',
            )

            news_analyst_task = Task(
                description=f'''Using the following news data:
{news_context}

Analyze recent news and developments by:
1. Evaluating the overall news sentiment (positive/negative/neutral)
2. Identifying major news events that could impact the asset
3. Analyzing corporate announcements and industry trends
4. Assessing market reactions to recent news
5. Identifying upcoming events that could affect the asset
6. Providing detailed reasoning for sentiment conclusions
7. Including source citations for each news item analyzed''',
agent=news_analyst,
expected_output='''## 📰 News Analysis Report

### 🎯 Overall Sentiment: [score] (Confidence: [level]%)

### ✨ Positive Factors:
[List positive factors with citations]
- Factor 1 [Source: URL/publication name]
- Factor 2 [Source: URL/publication name]

### ⚠️ Negative Factors:
[List negative factors with citations]
- Factor 1 [Source: URL/publication name]
- Factor 2 [Source: URL/publication name]

### 📅 Recent Major Events:
[List and analyze events with citations]
- Event 1: [Description] [Source: URL/publication name]
- Event 2: [Description] [Source: URL/publication name]

### 🔮 Future Catalysts:
[List upcoming events with citations]
- Catalyst 1: [Description] [Source: URL/publication name]
- Catalyst 2: [Description] [Source: URL/publication name]

### 📈 Industry Trends:
[Analysis of trends with citations]

### 💭 Detailed Reasoning:
[Your analysis with supporting citations]

### ⚡ Key Risks:
[List risks with citations where applicable]''',
            )

            reddit_analyst_task = Task(
                description=f'''Using the following Reddit data:
{reddit_context}

Analyze Reddit sentiment by:
1. Evaluating overall sentiment across relevant subreddits
2. Identifying main bullish and bearish arguments
3. Analyzing trending topics and concerns
4. Assessing sentiment change over time
5. Evaluating discussion quality and credibility
6. Providing detailed reasoning for sentiment conclusions''',
agent=reddit_analyst,
expected_output='''## 💬 Reddit Sentiment Analysis

### 🎯 Overall Sentiment: [score] (Confidence: [level]%)

### 🐂 Bullish Arguments:
[List main bullish points]

### 🐻 Bearish Arguments:
[List main bearish points]

### 🔥 Trending Topics:
[List hot topics]

### 📊 Sentiment Trends:
[Trend analysis]

### ⭐ Quality Analysis:
[Discussion quality assessment]

### 👨‍💼 Expert Opinions:
[Notable expert views]

### 💭 Analysis Reasoning:
[Your detailed analysis]

### ⚠️ Risk Factors:
[List potential risks]''',
            )

            crew = Crew(
                agents=[techninal_analyst, news_analyst, reddit_analyst],
                tasks=[techninal_analyst_task, news_analyst_task, reddit_analyst_task],
                process=Process.sequential,
                verbose=True,
            )

            result = crew.kickoff()

            technical_result = techninal_analyst_task.output.raw
            news_result = news_analyst_task.output.raw
            reddit_result = reddit_analyst_task.output.raw

            output_content = f"""# 📑 Asset Analysis Report for {input_asset}
⏰ Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}



{technical_result}

{news_result}

{reddit_result}

🏁 End of Report
            """

            # Save to result.md
            output_path = Path('result.md')
            output_path.write_text(output_content)

            print(f"\nAnalysis saved to {output_path.absolute()}")
            update_status('Analyzing Final Results', 'completed', output_content, is_all_completed=True)

        except Exception as e:
            update_status('Analyzing Final Results', 'failed', str(e))
            print(f"Error during analysis: {e}")

    # Start the analysis in a new thread
    analysis_thread = threading.Thread(target=run_analysis)
    analysis_thread.start()

    return analyze_id

# Example usage
if __name__ == "__main__":
    input_asset = os.getenv('INPUT_ASSET')
    analyze_crypto_asset(input_asset)
