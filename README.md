# Description

A simple Korean stock trading bot used by CREON API (대신증권).

# Trading Algorithm

The trading algorithm is fairly simple, the program checks the current price of target stocks (defined in stock_list.txt) and automatically buys and sells stock by analyzing the moving average of target stocks. For more details, please check the ipynb in the repository.

# How to Run

The program requires the CREON PLUS installed in the running environment. [Link](https://money2.creontrade.com/E5/WTS/Customer/GuideTrading/CW_TradingSystemPlus_Page.aspx?m=9505&p=8815&v=8633)

Then change the credential information in AutoConnect.py

Lastly, run the main.py to start the program. All the trading history will be stored in Record.csv
