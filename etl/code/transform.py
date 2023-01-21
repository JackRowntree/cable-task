import pandas as pd


def transform(data):
    aggregated = calculate_top_10_shared_postcodes(data)
    return aggregated


def calculate_top_10_shared_postcodes(df):
    """
    Find top 10 most commonly shared postcodes
    """
    aggregated = df.groupby("postal_code", as_index=False).user_id.count().head(10)
    return aggregated
