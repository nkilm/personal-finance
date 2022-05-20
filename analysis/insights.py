import pandas as pd

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
    