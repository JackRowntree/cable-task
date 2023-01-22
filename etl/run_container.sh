#!/usr/bin/env bash

pytest test
python run_etl.py
python show_results.py