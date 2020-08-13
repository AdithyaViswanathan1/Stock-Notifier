# Stock-Notifier
Notifies you if a stock price goes below a certain value

# Cron Commands
PYTHONPATH=/usr/bin/python3\
\* \* \* \* \* cd ~/PycharmProjects/stock_notifier && /usr/local/bin/python3 main.py >> ~/PycharmProjects/stock_notifier/cron/cron.txt 2>&1

# What I Learned
 * Utilizing Python Libraries for Stock Analysis
 * Setting up as Cron Job
 * Sending text messages using Twilio
