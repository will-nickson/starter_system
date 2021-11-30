import requests
import mysql.connector as mysql
import os


db_connection = mysql.connect(
        host=os.environ.get('MYSQL_HOST'),
        user=os.environ.get('MYSQL_USER'),
        password=os.environ.get('MSQL_PASSWORD'),
        database=os.environ.get('BTC_DATA')
)

cursor = db_connection.cursor()

historical_data = requests.get('https://ftx.com/api/markets/BTC/USD/candles?resolution=86400').json()
# print(historical_data)

def insert_data(data):
    for i in data['result']:
        sql = 'insert into btcusd (time, open, high, low, close, volume) values (%s, %s, %s, %s, %s, %s)'
        val = (i['time'], i['open'], i['high'], i['low'], i['close'], i['volume'])
        cursor.execute(sql, val)

    db_connection.commit()
    print(cursor.rowcount, "records inserted...")

insert_data(historical_data)
