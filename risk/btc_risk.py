import os
import sys
import statistics
import mysql.connector as mysql

conn = mysql.connect(
    host=os.environ.get('MYSQL_HOST'),
    user=os.environ.get('MYSQL_USER'),
    password=os.environ.get('MSQL_PASSWORD'),
    database=os.environ.get('BTC_DATA')
)

cursor = conn.cursor()

def get_25_day_returns():
    data = []
    cursor.execute('select close from btcusd order by start_time desc limit 25;')
    result = cursor.fetchall()
    for r in result:
        data.append(r[0])
    return data

data = get_25_day_returns()
std = statistics.stdev(data)
pts = statistics.pstdev(data)
print(std)
print(pts)
