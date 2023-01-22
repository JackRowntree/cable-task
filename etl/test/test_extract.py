from code.extract import Schema 

def test_pre_extract():
    pass


def test_extract():
    pass


def test_read_raw_data():
    pass


def test_handle_incoming_batch():
    pass

def test_schema_postal_code_regex_check(mock_extract_data):
	Schema.postal_code_regex_check(mock_extract_data.postal_code)

