# AlgoTrading
A fully automated, algorithmic trading system that operates in the cryptocurrency market on Binance.

## Description
The algorithmic trading system I have developed trades across 17 different cryptocurrencies in the Binance Futures market. The script is hosted on Amazon Web Services (AWS), and runs 24/7.
The program:
- Is fully automatic, meaning it executes trades without any human intervention.
- Utilises technical analysis, meaning it uses intraday patterns in pricing and volume to execute trades as opposed to fundamental analysis, which attempts to measure the intrinsic value of a currency.
- Is a short term trading strategy. The majority of positions are held for less than an hour.

Due to the sensitive and proprietary nature of the trading system, I cannot include certain files in the repository. I have included the file responsible for initializing and updating data to provide an overview of how the system works.

## Trading System
A general overview of how the trading system operates is as follows:
1. Upon startup, the program requests relevant historical data from Binance by use of its API.
2. This historical data is used to generate technical indicators, which inform trading decisions.
3. Binance provides a websocket, from which the trading system receives data approximately every second. As new data is collected, the technical indicators are updated accordingly.
