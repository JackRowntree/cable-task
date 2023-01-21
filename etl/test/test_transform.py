import pandas as pd


def test_calculate_top_10_shared_postcodes(mock_extract_data):
    aggregated = calculate_top_10_shared_postcodes(mock_extract_data)
    expected = pd.DataFrame({"postal_code": ["A", "B", "C"], "count": [3, 2, 1]})
    pd.testing.assert_frame_equal(aggregated, expected)


def test_transform():
    pass
