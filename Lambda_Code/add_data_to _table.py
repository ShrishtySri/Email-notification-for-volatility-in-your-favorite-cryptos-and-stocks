import json
from yahoo_fin.stock_info import *
import boto3
from boto3.dynamodb.condition import key
from decimal import Decimal
import time
import os

tickers=["BTC-USD","ETH-USD","ADA-USD","AMZN","^NSEI","^BSESN","TCS","HDFCBANK.NS"]
table_name=os.environ['TickerData']

def prices(tickers):
    fav_stocks={}
    for symbol in tickers:
        price= get_live_price(symbol)
        fav_stocks[symbol]=round(price,2)
    return(fav_stocks)
    
def add_items(item):
    ddb_data=json.loads(json.dumps(item),parse_float=Decimal)
    dynamdb=boto3.resource('dynamdb')
    table=dynamdb.Table(table_name)
    for key in ddb_data:
        response=table.put_item(
            Item={
                'ticker':key,
                'timestamp':int(round(time.time()*1000)),
                'price':ddb_data[key]
            }
        )
    return response
    
def lambda_handler(event, context):
    # TODO implement
    try:
        dynamdb=boto3.resource('dynamdb')
        items=prices(tickers)
        add_items(items)
    except Exception:
        return None
