import mysql.connector
from mysql.connector import MySQLConnection, Error
from configparser import ConfigParser
import csv
import pandas as pd
import functions


def query_with_fetchmany():
    '''
    -----------------------------------------------------------------------
    Funtion that connects to data base.
    -----------------------------------------------------------------------
    INPUTS:  None
    OUTPUTS: None.

    LOCAL VARIABLES AND ARGUMENTS:
        data_df     = data frame, containing the articles info.
        dbconfig = dictionary, containing log in information.
        conn     = mysql connector.
        cursor   = classm mysql connector cursor.
        row      = tuple, with the data instantiation from the database.
        e        = exect error handler.
        list_abstracts = list, list with abstracts data in tuples.
        df_abstracts   = dataframe, contains all the abstracts extracted from
                         the database.
    -----------------------------------------------------------------------
    '''
    data_df = pd.DataFrame(columns=['A', 'b', 'C'])

    try:
        print('Connecting to MySQL database...')
        dbconfig = functions.read_db_config()
        conn = MySQLConnection(**dbconfig)

        if conn.is_connected():
            print('connection established. \n')
            cursor = conn.cursor()



            # query_vars = "SELECT issn, journal, abstract, LastName, FirstName, year FROM abstract "
            # table_1 = "INNER JOIN authors ON abstract.pmid = authors.pmid "
            # table_2 = "INNER JOIN doc ON abstract.pmid = doc.pmid"
            # query = query_vars + table_1 + table_2

            query = "SHOW SCHEMAS"

            cursor.execute(query)

            #list_abstracts = functions.iter_row(cursor, 10)
            for row in functions.iter_row(cursor, 100):
                print(row)
        else:
            print('connection failed. \n')

    except Error as e:
        print(e)

    finally:
        # Fix roblem closing the cursor.
        #cursor.close()
        conn.close()
        print('Connection closed.')

        # Save list to a data frame.
        # df_abstracts = pd.DataFrame(list_abstracts,
        #                             columns=["issn", "journal", "abstract", "LastName", "FirstName", "year"])
        # with open("./data/abstracts.csv", "w") as f:
        #     df_abstracts.to_csv(f, header=True)


if __name__ == '__main__':
    query_with_fetchmany()