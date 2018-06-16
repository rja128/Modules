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

def engine(database, user, password, sqlServer='localhost'):
    if isinstance(sqlServer, str):
        sqlServer = sqlServer
    else:
        sqlServer = str(sqlServer)

    engine = create_engine('mysql+pymysql://{}:{}@{}/{}'.format(user, password, sqlServer, database), echo=True, pool_recycle=3600)
    return engine

def delAllTables(engine):
    dfListTables = pd.read_sql('show tables', engine)

    print(dfListTables)

    if dfListTables.empty:
        return None

    for tables in dfListTables.ix[:,0]:
        print(tables)

        if "Tables_in" in tables:
            continue 

        connection = engine.connect()
        result = connection.execute('DROP TABLE `{}`;'.format(tables))
        connection.close()

def addNoDuplicates(table, dfNew, engine):

     dfNew.to_sql('myTempTable', engine, if_exists='replace')

     connection = engine.connect() 
     connection.execute('INSERT IGNORE INTO {} SELECT * FROM myTempTable;'.format(table))
     connection.execute('DROP TABLE myTempTable;')
     connection.close() 


