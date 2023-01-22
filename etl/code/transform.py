import pandas as pd


def transform(data):
    """
    Runs transform functions on data.
    More functionality could be easily added here
    """
    aggregated = calculate_top_10_shared_postcodes(data)
    return aggregated


def calculate_top_10_shared_postcodes(df):
    """
    Find top 10 most commonly shared postcodes
    """
    aggregated = (
        df.groupby("postal_code", as_index=False)
        .user_id.nunique()
        .rename(columns={"user_id": "count"})
        .sort_values("count", ascending=False)
        .reset_index(drop=True)
        .head(10)
    )
    return aggregated
