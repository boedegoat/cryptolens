# CryptoLens

## Overview

This web-based tool is designed to automate cryptocurrency research by analyzing technical data, news, and Reddit sentiment for a specific crypto asset. Users simply input the cryptocurrency they want to research, and the tool generates a comprehensive final analysis report. Additionally, users can ask follow-up questions to an AI assistant if they have doubts about the report, making the research process effortless and highly informative.

## The Problem

Many individuals make impulsive cryptocurrency investments due to Fear of Missing Out (FOMO), often without conducting adequate research. This behavior can lead to financial losses and uninformed decision-making. Manually analyzing technical data, staying updated with news, and gauging sentiment from platforms like Reddit can be time-consuming and challenging for the average user.

## Our Solution

Our platform automates the research process by providing:

-   **Technical Analysis**: In-depth examination of price trends, trading volume, and other key metrics.
-   **News Analysis**: Summarized insights from the latest news related to the crypto asset.
-   **Reddit Sentiment Analysis**: A breakdown of public sentiment from discussions and trends on Reddit.

The solution generates a comprehensive report for any specified cryptocurrency. For additional clarity, users can interact with an AI assistant to ask questions or delve deeper into the report.

## How to Use

1. **Input the Crypto Asset**:
    - Enter the name or symbol of the cryptocurrency you want to research.
2. **Wait for the Analysis**:
    - Sit back while the tool collects and processes data.
3. **Review the Final Report**:
    - Receive a detailed analysis covering technical data, news, and sentiment.
4. **Ask Follow-Up Questions**:
    - Use the AI assistant to clarify or explore specific aspects of the report.

## Future Plans

1. **Enhanced Data Sources**:
    - Incorporate additional data sources for a more robust analysis.
2. **Mobile App Development**:
    - Develop a mobile version of the platform for on-the-go access.
3. **Portfolio Tracking**:
    - Add features for tracking and analyzing entire cryptocurrency portfolios.
4. **Real-Time Alerts**:
    - Introduce notifications for significant changes in sentiment, news, or technical indicators.
5. **Multi-Language Support**:
    - Expand accessibility by supporting multiple languages.

## Start Local Development

Make sure you have `python3` and `node` installed on your machine.

1. fill `.env` in `backend` folder with the following

    ```
    # ---------------- OPENAI API KEY ----------------
    OPENAI_API_KEY=your-openai-api-key

    # ---------------- REDDIT API KEY ----------------
    REDDIT_CLIENT_ID=your-reddit-client-id
    REDDIT_CLIENT_SECRET=your-reddit-client-secret
    REDDIT_APP_NAME=your-reddit-app-name

    # ---------------- ALPHA VANTAGE API KEY ----------------
    ALPHA_VANTAGE_API_KEY=your-alpha-vantage-api-key

    # ---------------- NEWS API KEY ----------------
    NEWS_API_KEY=your-news-api-key
    ```

1. insert your `firebase_config.json` in `backend` folder

1. fill `.env.local` in `frontend` folder with the following

    ```
    OPENAI_API_KEY=your-openai-api-key
    ```

1. `cd` to `backend` folder and run the following commands

    ```
    pip install -r requirements.txt
    python server.py # start the backend server
    ```

1. `cd` to `frontend` folder and run the following commands

    ```
    npm install
    npm run build
    npm start # start the frontend server
    ```
