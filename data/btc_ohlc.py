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

response = requests.get('https://ftx.com/api/markets/BTC/USD/candles?resolution=86400').json()
# print(response)
data = response['result']
# print(data)

def insert_data(data):
    for i in data:
        sql = 'insert into btcusd (start_time, time, open, high, low, close, volume) values (%s, %s, %s, %s, %s, %s, %s)'
        val = (i['startTime'], i['time'], i['open'], i['high'], i['low'], i['close'], i['volume'])
        cursor.execute(sql, val)

    db_connection.commit()
    print(cursor.rowcount, "records inserted...")

insert_data(data)
