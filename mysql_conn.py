import os
import mysql.connector as mysql


def connect():
    """Connect to MySQL"""

    try:
        conn = mysql.connect(
                host=os.environ.get('MYSQL_HOST'),
                user=os.environ.get('MYSQL_USER'),
                password=os.environ.get('MSQL_PASSWORD'),
                database=os.environ.get('BTC_DATA')
        )

        return conn

    except Exception as error:
        print(error)

if __name__ == "__main__":
    connect()
