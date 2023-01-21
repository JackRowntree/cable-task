from extract import extract, pre_extract
from transform import transform
from load import load


def run_etl():
    """
    Runs E, T and L
    """
    pre_extract()
    extracted_df = extract()
    transformed_df = transform(extracted_df)
    load(transformed_df)


if __name__ == "__main__":
    run_etl()
