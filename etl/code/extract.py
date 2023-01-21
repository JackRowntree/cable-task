from common import read_data, push_data_to_db
import sqlite3
import pandas as pd

FPATH = '/etl/data/enhanced_synthetic_data_2.csv'
engine = None
CON_RAW = sqlite3.connect('raw_data.db')
CON_EXTRACT = sqlite3.connect('extract_data.db')

def pre_extract():
	data = read_incoming_batch()
	print(data)
	push_data_to_db(data, 'raw_data', CON_RAW)


def extract():
	df = read_raw_data()
	apply_schemas(df)
	run_qa_checks(df)
	print(df)
	return df


def read_raw_data():
	"""
	Reads raw data from db
	"""
	return read_data(CON_RAW,'raw_data')


def read_incoming_batch():
	"""
	Currently just reads full dataset from path, but functionality could be changed to fit any data ingestion circumstances!
	"""
	data = pd.read_csv(FPATH)
	return data

def apply_schemas(df):
	pass 

def run_qa_checks(df):
	pass