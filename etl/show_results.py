from code.common import read_data
import sqlite3

CON_LOAD = sqlite3.connect("sqlite/transformed_data.db")

def show_results():
    """
    Reads aggregated data
    """
    results = read_data(CON_LOAD,'transformed_data')
    print(results)

if __name__ == "__main__":
    show_results()
