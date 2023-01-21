from extract import extract, pre_extract
from transform import transform
from load import load


def run_etl():
	"""
	Runs E, T and L
	"""
	pre_extract()
	extracted_dfs = extract()
	transformed_dfs = transform(extracted_dfs)
	load(transformed_dfs)


if __name__ == "__main__":
    run_etl()
