from common import push_data_to_db
import sqlite3

CON_LOAD = sqlite3.connect("transformed_data.db")


def load(df):
    push_data_to_db(df, "transformed_data", CON_LOAD)
