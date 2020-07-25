import os
import pymysql

# get username from gitpod workspace
username = os.getenv('GP_USER')

# connet to the database
connection = pymysql.connect(
    host='localhost', user=username, password='', db='Chinook')

try:
    # run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # close the connection, refardless of whether the above was succesful
    connection.close()
