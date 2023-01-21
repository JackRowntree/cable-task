import pandas as pd


def read_data(connection, table):
    df = pd.read_sql_query(f"SELECT * FROM {table}", connection)
    return df


def push_data_to_db(df, table, connection, if_exists="fail"):
    df.to_sql(table, connection, index=False, if_exists=if_exists)
    print("pushed)")
