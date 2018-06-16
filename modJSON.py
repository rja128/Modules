import os
import pickle
import requests
import urllib.request
import datetime as dt
import csv
import json
import modules as mod
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import pandas_datareader.data as web
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Float
from sqlalchemy.orm import sessionmaker, scoped_session
import sys
sys.path.insert(0, '/home/epimetheus/Programming/Python/TradeKingApi')
import TradeKingAPI as api

def printJSON(jsonDict):
    prettyJSON = json.dumps(jsonDict, sort_keys=True, indent=4)

    print(prettyJSON)

##Formats JSON response from api call, created for TradekingAPI but can be modified
def formatResponse(response):
    ##Content from the response format bytes
    holder1 = response.content

    ##Contest from the response converted from bytes to string
    holder2 = holder1.decode("utf-8")

    ##Loads string into json format dict
    result = json.loads(holder2)

    return result

