import pymysql
import pandas as pd 
from pandas import DataFrame
import sys
import numpy as np 
import pandas_datareader.data as pdr 


#Function to upload CSV file to specified table in MySQL
def csv_to_mysql(load_sql, host, user, password):

    try:

        con = pymysql.connect(host=host,
                                user=user,
                                password=password,
                                autocommit=True,
                                local_infile=1)

        print('Connected to DB: {}'.format(host))

        # Create cursor and execute Load SQL
        cursor = con.cursor()
        cursor.execute(load_sql)
        print('Succuessfully loaded the table from csv.')
        con.close()
       
    except Exception as e:

        print('Error: {}'.format(str(e)))
        sys.exit(1)

#asking to upload another CSV
def replay():

    return input('Do you want to shape/upload another csv?\n').lower().startswith('y')

while True:

    try:

        csv_input = str(input('Enter the file name of the csv:\n').lower())

        df = pd.read_csv(f'C:/Users/pat/Downloads/{csv_input}.csv')

        #reshaping the file to bring values to rows and metrics to columns
        value_rows = df.pivot_table('Values', ['Date', 'Ticker'], 'Metrics')

        #reordering the file to mirror my stock price table 
        ordered_columns = value_rows.reindex(['Close', 'Open', 'High', 'Low', 'Adj Close', 'Volume'], axis=1)

        print(ordered_columns)

        ordered_columns.to_csv(r'C:/Users/pat/Desktop/stock prices/{}.csv'.format(csv_input))

        upload_sql = str(input('Done shaping file for sql, would you like to upload to sql here?\n').lower())

        if upload_sql[0] == 'y':

            table_name = str(input('Specify what table you would like to upload too:'))

            load_sql = """LOAD DATA LOCAL INFILE {} INTO TABLE {}} 
            FIELDS TERMINATED  BY ',' ENCLOSED BY '"' IGNORE 1 LINES;""".format(csv_input,table_name)

            host = '127.0.0.1'
            user = 'root'
            password = 'password'
            csv_to_mysql(load_sql, host, user, password)
            
        elif replay():

            continue

        else: 

            break

    except:
        print('Something went wrong, try again!')
        pass
               
