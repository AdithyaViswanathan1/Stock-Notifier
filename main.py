from decimal import Decimal
from pip._vendor.distlib.compat import raw_input
from yahoo_fin import stock_info as si
from yahoo_fin.stock_info import get_data
from twilio.rest import Client

#if program is NOT a cron job, ask user to enter which stock to track
#stock = raw_input("Which stock do you want to track? (Ex: AAPL) ")

#if program is going to be used as cron job, set stock yourself
stock = "sdc"

#Live stock price
current_stock_price = float(si.get_live_price(stock))
#print("Current stock price: " + str(current_stock_price))

#if program is NOT a cron job, ask user for minimum stock price they would like to go to
#min_stock_price = float(raw_input("At what stock price would you like to be notified? "))

#if program is cron job, set minimum threshold yourself
min_stock_price = 8.5

#dropped_amount = starting_stock_price - float(si.get_live_price(stock))
if(current_stock_price < min_stock_price):
    message = "Alert! "
    message += stock.upper() + " has dropped to $" + "{:.2f}".format(current_stock_price)
    print(message)

    #Code for sending as text message
    account_sid = 'sid'
    auth_token = 'token'
    client = Client(account_sid, auth_token)

    #message = client.messages \
                #.create(
                #     body=message,
                #     from_='from_number',
                #     to='to_number'
                # )

    #print(message.sid)






