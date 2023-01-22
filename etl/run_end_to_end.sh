#!/usr/bin/env bash

printf "##########\nRunning unit tests\n##########\n"
pytest test
printf "##########\nRunning ETL\n##########\n"
python run_etl.py
printf "##########\nQuerying insights in output db\n##########\n"
python show_results.py