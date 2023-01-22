from code.common import read_data, push_data_to_db
import sqlite3
import pandas as pd
import pandera as pa
from pandera.typing import Series

FPATH = "/etl/data/enhanced_synthetic_data_2.csv"
CON_RAW = sqlite3.connect("./sqlite/raw_data.db")


class Schema(pa.SchemaModel):
    """
    Defines schema and checks. Can be expanded with more schema info and checks
    """

    postal_code: Series[str] = pa.Field()

    @pa.check("postal_code")
    def postal_code_regex_check(cls, series: Series[str]) -> Series[bool]:
        """check that postcodes match the uk gov regex!"""
        return series.str.match(
            "([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})"
        )


def pre_extract():
    """
    This function handles the ingestion of raw data.
    A table with a primary key on user_id is created if not existing,
    a date of ingestion is added, and data is appended to db.
    The goal of this step is to load whatever is coming in into a datastore
    in its raw form - in reality something cheap like S3
    """
    execute_create_table_statemtents()
    data = read_incoming_batch()
    add_ingested_date(data)
    push_data_to_db(data, "raw_data", CON_RAW, "append")


def extract():
    """
    Reads totality of raw data, runs checks, returns data
    """
    df = read_raw_data()
    apply_schemas_and_checks(df)
    df = df.drop_duplicates('user_id')
    return df


def read_raw_data():
    """
    Reads raw data from db
    """
    return read_data(CON_RAW, "raw_data")


def read_incoming_batch():
    """
    Currently just reads full dataset from path, but functionality could be changed to fit any data ingestion circumstances!
    """
    data = pd.read_csv(FPATH)
    return data


def apply_schemas_and_checks(df):
    """
    Runs pandera validation on df.
    Try/catch is just to provide visibility on the results without stopping the code.
    """
    try:
        Schema.validate(df, lazy=True)
    except pa.errors.SchemaErrors as err:
        print("Schema errors and failure cases:")
        print(err.failure_cases)


def add_ingested_date(df):
    """
    Adds date ingested to raw data
    """
    df["ingested_at"] = pd.Timestamp.now()


def execute_create_table_statemtents():
    """
    Creates a table with user_id as primary key
    """
    c = CON_RAW.cursor()
    c.execute(
        """
		CREATE TABLE IF NOT EXISTS raw_data (
		user_id text,
		signup_time text,
		name text,
		address_lines text,
		postal_area	text,
		postal_code	text,
		country text,
		email text,	
		phone_number text,	
		account_status text,
		date_of_birth text,
		customer text,
		updated_at text,
		ingested_at text
		);
		"""
    )
