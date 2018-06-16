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

def indexDatetime(df):
    dfTest = df.index
    df.index = pd.to_datetime(dfTest)
    df.index.dtype

    return df

def rotateJSON_to_DF(json):
    df = pd.io.json.json_normalize(json)

    return df


