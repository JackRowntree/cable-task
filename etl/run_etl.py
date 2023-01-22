from code.extract import extract, pre_extract
from code.transform import transform
from code.load import load


def run_etl():
    """
    Runs Pre-E, E, T and L.
    """
    pre_extract()
    extracted_df = extract()
    transformed_df = transform(extracted_df)
    load(transformed_df)


if __name__ == "__main__":
    run_etl()
