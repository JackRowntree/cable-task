import pandas as pd


def read_data(connection, table):
	"""
	SELECT * from a given table. Not the most flexible function but OK for now
	"""
    df = pd.read_sql_query(f"SELECT * FROM {table}", connection)
    return df


def push_data_to_db(df, table, connection, if_exists="fail"):
	"""
	Push a dataframe to db. Make if_exists default to fail to enforce specificity!
	"""
    df.to_sql(table, connection, index=False, if_exists=if_exists)