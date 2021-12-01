import requests
import mysql.connector as mysql
import os
from datetime import datetime


db_connection = mysql.connect(
        host=os.environ.get('MYSQL_HOST'),
        user=os.environ.get('MYSQL_USER'),
        password=os.environ.get('MSQL_PASSWORD'),
        database=os.environ.get('BTC_DATA')
)

cursor = db_connection.cursor()


response = requests.get('https://ftx.com/api/markets/BTC/USD/candles?resolution=86400').json()
ftx_data = response['result']

def get_mysql_data():
    cursor.execute('select start_time from btcusd order by start_time desc limit 1;')
    result = cursor.fetchall()
    return result[0][0]

recent = get_mysql_data()

def get_data_to_insert():
    d = []

    sorted_data = sorted(ftx_data, key=lambda x: x['time'], reverse=True)
    date = sorted_data[0]['startTime'][:19]
    date_str = str(date)
    date_str.replace('T', ' ')
    formatted = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

    # if sorted_data[0]['time'] >= recent:
        # print('true')
        # d.append(i)

    print(d)
    return d


get_data_to_insert()

def insert_data(data):
    for i in data:
        sql = 'insert into btcusd (start_time, time, open, high, low, close, volume) values (%s, %s, %s, %s, %s, %s, %s)'
        val = (i['startTime'], i['time'], i['open'], i['high'], i['low'], i['close'], i['volume'])
        cursor.execute(sql, val)

    db_connection.commit()
    print(cursor.rowcount, "records inserted...")

# insert_data(data)
