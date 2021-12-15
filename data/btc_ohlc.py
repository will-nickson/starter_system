import os
import sys
import requests
import mysql.connector as mysql
from datetime import datetime

ftx_data = requests.get('https://ftx.com/api/markets/BTC/USD/candles?resolution=86400').json()
# print(ftx_data)

conn = mysql.connect(
    host=os.environ.get('MYSQL_HOST'),
    user=os.environ.get('MYSQL_USER'),
    password=os.environ.get('MSQL_PASSWORD'),
    database=os.environ.get('BTC_DATA')
)

cursor = conn.cursor()

def get_mysql_data():
    cursor.execute('select start_time from btcusd order by start_time desc limit 1;')
    result = cursor.fetchall()
    print(result)
    return result[0][0]

recent = get_mysql_data()

def format_ftx_data():
    d = []
    sorted_data = sorted(ftx_data['result'], key=lambda x: x['time'], reverse=True)

    for i in sorted_data:
        date = i['startTime'][:10]
        formatted = datetime.strptime(date, '%Y-%m-%d')
        if formatted > recent:
            d.append(i)

    return d

new_data = format_ftx_data()

def insert_data(new_data):
    for i in new_data:
        sql = 'insert into btcusd (start_time, time, open, high, low, close, volume) values (%s, %s, %s, %s, %s, %s, %s)'
        val = (i['startTime'], i['time'], i['open'], i['high'], i['low'], i['close'], i['volume'])
        cursor.execute(sql, val)

    conn.commit()
    print(cursor.rowcount, "records inserted...")

insert_data(new_data)
