##############################################
# This file containg a series of helper functions
# To aid in the analysis of p-values contained in 
# text. 
##############################################

#### Libraries ###############################
import pandas as pd
import re
import mysql.connector
from mysql.connector import MySQLConnection, Error
from configparser import ConfigParser
import csv
import pandas as pd


### Functions #################################
def read_db_config(filename='config.ini', section='mysql'):
    '''
    -----------------------------------------------------------------------
    Read database configuration file and return a dictionary object.
    -----------------------------------------------------------------------
    INPUTS:
        filename  = string, configuration file "config.ini"
        section   = string, section to red from the "config.ini"

    OUTPUTS: None.

    LOCAL VARIABLES AND ARGUMENTS:
        parser    = parser, object to parse the "config.ini".

    RETURNS:
        db        = dictionary, a dictionary of database parameters.
    -----------------------------------------------------------------------
    '''
    # Creates parser and read the config.ini file.

    parser = ConfigParser()
    parser.read(filename)

    # get section, default to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return db

read_db_config()


def iter_row(cursor, size=5):
    '''
    -----------------------------------------------------------------------
    Read database configuration file and return a dictionary object.
    -----------------------------------------------------------------------
    INPUTS:
        cursor  = classm mysql connector cursor.
        size    = int, Number of rows to extract from database. Input to
                       fetchmany()
    OUTPUTS:
        none.

    LOCAL VARIABLES AND ARGUMENTS:
        rows    = list, contained the retrieved data from the database.

    RETURNS:
        rows    = list, contained the retrieved data from the database.
    -----------------------------------------------------------------------
    '''
    for rows in range(size):
        rows = cursor.fetchmany(size)
        if not rows:
            break
        else:
            return rows


def extract_p_values(text, label):
    '''
    -----------------------------------------------------------------------
    (Prototipe) A function to extract p values from a string of text.
    -----------------------------------------------------------------------
    INPUTS:
        text  = Text to be parsed.
        label  = Section to be parsed.
        
    RETURNS:
        pvalues    = list, contained the pvalues retrieved from text.
    -----------------------------------------------------------------------
    '''
    if type(text) is str:
        regex = re.compile("[^a-zA-Z0-9*#†_][Pp][\s]*[=<>≤≥][\s]*[01]?[.][\d]+")
        matches = regex.findall(text)
        pvals = []
        strip the first character, then the 'p' or 'P'
        for i, match in enumerate(matches):
        match = "".join(match.split()) # remove all whitespace

        # now extract just the 'p=' part...
        regex = re.compile("[Pp][\s]*[=<>≤≥][\s]*[01]?[.][\d]+")
        match = regex.findall(match)[0]
        operator = match[1]
        val = match[2:]
        decimal_places = len(val.split('.')[1])
        val = float(val)
        if val <= 1.0:
        pval = [operator, val, decimal_places, label]
        pvals.append(pval)

        return(pvals)

