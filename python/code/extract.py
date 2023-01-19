from common import read_data,push_data_to_db

FPATH = ''
engine = None

def pre_extract():
	data = pd.read_csv(FPATH)
	push_data_to_db(data)

def extract():
	df = read_raw_data(engine)
	return df


def read_raw_data():
	"""
	Reads raw data from db
	"""
	read_data(engine,'raw')