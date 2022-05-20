import pandas as pd
from datetime import datetime

df = pd.read_csv("./data/transactions.csv")

def transactions_list():
    """
    List of all transactions in the form of dataframe.
    """

    # df = df["index","Transaction Date","Description","Ref No./Cheque No","Debit"]

    return df

def summary():
    credits = df["Credit"].sum()
    debits = df["Debit"].sum()
    return credits,debits

def month():
    date = df["Transaction Date"][len(df["Transaction Date"])-1]
    months_in_year = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    print(date)
    datem = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    month = months_in_year[datem.month-1]
    year = datem.year
    return month,months_in_year