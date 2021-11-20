# Email-notification-for-volatility-in-your-favorite-cryptos-and-stocks
In this application, we will be fetching live crypto and stocks data from Yahoo-finance for required tickers under required time interval using AWS Lambda in Python and store in dynamoDB and compared with the most recent data for change in the price. If there is a change in the price of certain percent then an email is sent to the user.
I have used multiple AWS services to build this serverless system on cloud. These include AWS Lambda, DynamoDB, SES, CloudWatch events.

Overview:
CloudWatch events trigger on minute intervals or hour intervals. For every trigger or message, it invokes Lambda function and it gets the live Stock/Crypto price data from Yahoo Finance and adds data as records to the DynamoDB table.
For every row or record added in the table for a particular stock/crypto, DynamoDB streams will trigger another Lambda function which performs a query on the DynamoDB table and compares the price from the new record to the most recent record. If the price rises or drops by a certain percent, lambda function will email the user using SES with the message on the price movement. Here, ticker is the partition key, timestamp is the sort key and price is an attribute.
