import pytest 
import pandas as pd 
@pytest.fixture
def mock_extract_data():
    return pd.DataFrame(
        {
            "user_id": [
                "A",
                "B",
                "C",
                "D",
                "E",
                "F",
            ],
            "postal_code": ["NW3 2YR", "NW3 2YR", "NW3 2YR", "HA7 3NU", "HA7 3NU", "blah"],
            "blah": [1, 2, 3, 1, 2, 3],
        }
    )

