'use server'

export async function analyzeCryptoAsset(prevState: FormData, formData: FormData) {
	const asset = formData.get('asset')

	// Simulate API call delay
	await new Promise((resolve) => setTimeout(resolve, 8000))

	// This is a mock result. In a real application, you would call your AI service here.
	const mockResult = `
# 📑 Asset Analysis Report for solana
⏰ Generated on: 2024-12-16 21:21:16

## 📊 Technical Analysis Report

### 🎯 TL;DR Summary:
🔍 Direction: 🐻 Bearish  
📊 Support: $213.26  
📈 Resistance: $227.56  
💡 Action: Sell (Confidence: 75%)  
⚡ Key Points:
- The overall trend is bearish with a series of lower highs and lower lows.
- Key indicators such as RSI and MACD are showing bearish signals.
- Price is below major moving averages, indicating downward momentum.

### 🎯 Current Trend Analysis:
The current trend for SOLUSDT is bearish. The price has been making lower highs and lower lows, which is a classic sign of a downtrend. The recent price action shows a failure to break above the resistance level of $227.56, reinforcing the bearish sentiment. The volume has been decreasing, indicating a lack of buying interest at higher levels.

### 📈 Support and Resistance Levels:
- **Support:** The immediate support level is at $213.26, which is the recent low. If this level is breached, the next support could be around $202.37, based on previous price action.
- **Resistance:** The immediate resistance is at $227.56, which is the recent high. A break above this level could see the price testing the next resistance at $234.70.

### 💰 Recommendation:
Based on the current analysis, the recommendation is to Sell with a confidence level of 75%. The bearish indicators and price action suggest further downside potential.

### 🔮 Price Predictions:
- **Short-term (1-7 days):** The price is likely to test the support level at $213.26. If this level holds, a minor bounce could occur, but the overall trend remains bearish.
- **Medium-term (1-3 months):** The price could continue to decline towards the $200 level if the bearish trend persists and support levels are breached.

### 📑 Technical Reasoning:
The RSI is currently at 44.37, which is below the neutral 50 level, indicating bearish momentum. The MACD is also negative, with the MACD line below the signal line, further confirming the bearish trend. The price is trading below the 50-day and 100-day moving averages, suggesting that the bears are in control. The ADX is at 23.42, indicating a weak trend, but the negative DI is higher than the positive DI, supporting the bearish outlook.

### 📉 Key Technical Indicators:
- **RSI:** 44.37 (Bearish)
- **MACD:** -0.41 (Bearish)
- **ADX:** 23.42 (Weak trend, but bearish)
- **EMA50:** 214.99 (Price below EMA, bearish)
- **SMA50:** 216.91 (Price below SMA, bearish)

### 📋 Historical Patterns:
The price has been in a downtrend since late November, with a significant drop from the highs of $256.91. The pattern of lower highs and lower lows is consistent with a bearish trend.

### ⚠️ Risk Factors:
- A sudden increase in buying volume could reverse the bearish trend.
- External market factors or news events could impact the price unexpectedly.
- If the price breaks above the resistance level of $227.56, it could invalidate the bearish outlook.

## 📰 News Analysis Report

### 🎯 Overall Sentiment: Negative (Confidence: 70%)

### ✨ Positive Factors:
- Ethereum Dev Max Resnick Defects to Solana, citing more potential energy in Solana [Source: CoinDesk](https://www.coindesk.com/tech/2024/12/09/ethereum-dev-max-resnick-defects-to-solana-citing-frustration)
- Stablecoin Trading Startup Perena Tries Its Luck on Solana, indicating interest in Solana's ecosystem [Source: CoinDesk](https://www.coindesk.com/business/2024/12/11/stablecoin-trading-startup-perena-tries-its-luck-on-solana)

### ⚠️ Negative Factors:
- Solana blockchain's popular web3.js npm package backdoored to steal keys, funds, posing security risks [Source: The Register](https://www.theregister.com/2024/12/05/solana_javascript_sdk_compromised/)
- Solana Library Supply Chain Attack Exposes Cryptocurrency Wallets, further highlighting security vulnerabilities [Source: Infosecurity Magazine](https://www.infosecurity-magazine.com/news/solana-library-supply-chain-attack/)

### 📅 Recent Major Events:
- Sol Strategies plans Nasdaq listing after a 2,336% stock surge since July on Canadian exchange, showing significant corporate movement within the Solana ecosystem [Source: Biztoc](https://biztoc.com/x/d65198fd07287eba)
- XRP Flips Solana, Topping $2 for First Time Since 2018, indicating a shift in market cap rankings [Source: Biztoc](https://biztoc.com/x/11549e96b7cb8d8f)

### 🔮 Future Catalysts:
- Popular NFT project Pudgy Penguins plans to launch a Solana-based token called PENGU within this year, which could drive interest and activity on the Solana blockchain [Source: Techmeme](https://www.techmeme.com/241205/p49)
- Ranger Finance Targets Crypto Perps Traders of 'Size' on Solana, potentially increasing Solana's DeFi market activity [Source: CoinDesk](https://www.coindesk.com/business/2024/12/12/ranger-finance-targets-crypto-perps-traders-of-size-on-solana)

### 📈 Industry Trends:
The Solana ecosystem is attracting new projects and developers, as seen with the defection of Ethereum developers and the launch of new startups like Perena. However, security concerns remain a significant issue, with recent backdoor attacks on Solana's web3.js library.

### 💭 Detailed Reasoning:
The overall sentiment for Solana is negative due to significant security vulnerabilities that have been exposed, which could undermine trust in the ecosystem. Despite positive developments such as new projects and developer interest, these are overshadowed by the potential risks associated with the recent security breaches. Additionally, Solana's market position has been challenged by XRP's recent surge, which could impact investor sentiment.

### ⚡ Key Risks:
- Security vulnerabilities in Solana's infrastructure could lead to loss of funds and erode user trust.
- Market competition from other cryptocurrencies like XRP could affect Solana's market cap and investor interest.
- Regulatory changes or adverse news could further impact the sentiment and valuation of Solana.

## 💬 Reddit Sentiment Analysis

### 🎯 Overall Sentiment: Mixed to Negative (Confidence: 65%)

### 🐂 Bullish Arguments:
- Solana is seen as a competitive player in the decentralized NASDAQ space due to its low cost, fast transactions, and acceptable decentralization.
- Solana has become the top choice for new developers, surpassing Ethereum, which indicates strong developer interest and potential for growth.
- The network's stability and governance are supported by a diverse group of holders, which could provide a solid foundation for future growth.
- Solana's DeFi ecosystem is gaining traction with both retail and institutional investors, aiming for a $250 price target.

### 🐻 Bearish Arguments:
- Concerns about the legitimacy of new developers, with some suspecting many are involved in creating rug-pulling memecoins.
- The Solana network is criticized for being clogged with rug pulls and scams, which could deter serious investors.
- Security vulnerabilities, such as the backdoor in the web3.js npm package, pose significant risks to user funds and trust.
- Solana's market position is challenged by competitors like XRP, which recently surpassed Solana in market cap rankings.

### 🔥 Trending Topics:
- Security concerns and scams on the Solana network.
- The influx of new developers and projects on Solana, including the Pudgy Penguins NFT project.
- Comparisons between Solana, Ethereum, and other competitors like SUI and SEI.
- The impact of market competition from other cryptocurrencies like XRP.

### 📊 Sentiment Trends:
- There is a growing concern about security issues and scams, which is negatively impacting sentiment.
- Despite security concerns, there is still interest in Solana's potential as a leading blockchain for new projects and developers.
- The sentiment is mixed, with some users optimistic about Solana's growth potential, while others are wary of the risks.

### ⭐ Quality Analysis:
- The discussion quality varies, with some insightful analysis on Solana's competitive position and potential, but also a significant amount of noise related to scams and memecoins.
- There is a need for more credible and detailed discussions to provide a clearer picture of Solana's prospects.

### 👨‍💼 Expert Opinions:
- Some experts highlight Solana's potential due to its competitive transaction costs and speed, but caution against security vulnerabilities.
- The defection of Ethereum developers to Solana is seen as a positive sign of Solana's growing appeal.

### 💭 Analysis Reasoning:
The sentiment around Solana is mixed to negative, primarily due to security vulnerabilities and concerns about scams on the network. While there is notable interest from developers and new projects, these positives are overshadowed by the risks associated with recent security breaches. The competitive landscape, with XRP surpassing Solana, adds to the uncertainty. Investors are advised to proceed with caution, considering both the potential and the risks.

### ⚠️ Risk Factors:
- Security vulnerabilities could lead to significant financial losses and damage to Solana's reputation.
- Intense competition from other cryptocurrencies could impact Solana's market position and investor interest.
- Regulatory changes or negative news could further affect sentiment and valuation.

🏁 End of Report

  `

	return mockResult
}
