# cable-task

## Requirements

A working docker installation

## How to run

`cd cable-task` and `docker-compose up`. This will run `etl/run_end_to_end.sh`, which:
1. Runs the test suite
2. Runs the etl code 
3. Runs the script querying the final output db

## Other info

This repo contains a short sample of the data supplied, so the repo is lightweight but still keeps everything coupled together. If you want to run on the full sample dataset, just `mv` the file into `cable-task/etl/data/enhanced_synthetic_data_2.csv`.

## Notes on the dataset

### Data quality appears to be an issue:

* user_id is duplicated
* Some email addresses contain whitespace
* Some phone numbers appear invalid
* Many users share same `customer` value, which is not necessarily an issue

### Data Governance
This dataset is full of personally identifiable info. That would obviously affect all decisions about where this pipeline moves data too, and indeed whether it could run at all. 


## Notes on the solution

### Notes on architecture
Data is ingested from a hardcoded path in the repo. Subsequent reads will keep appending ingested csv data into the raw db. Overall outline below + diagram:

1. pre-extract: incoming raw csv chunk appended to raw db
2. extract: full dataset read from raw db and deduplicated
3. transform: data aggregated
4. load: transformed data pushed to transformed db

![](/system_diagram.png?raw=true "Optional Title")

#### Datastore
I stuck to the sqlite brief - the dbs are persistent between runs of the container thanks to the volume, so raw data will keep being appended to the raw db, which is read by extract and deduplicated.
Normally I would have extended the docker-compose with a postgres service instead as I haven't used sqlite in years!

#### Pre-extract
The idea of the pre-extract phase is to `append` incoming chunks of data to a datastore, which will be read in totality in the extract step. This was my interpretation of a pipeline that can handle data ingestion over time in production. Adding a field indicating date of ingestion adds some context to this raw data. 

#### Extract
Sends a `SELECT * ` query to the pre-extract db. Runs `pandera` schema checks - I just added one to validate the postcodes which are later used for the transformations. However this functionality could be easily expanded for a proper schema/QA step. Ideally, the extract stage would push to a third `extract` db to store deduplicated data, however I didn't get round to this due to time shortage.

#### Transform
Runs a function calculating the top 10 most common postcodes.

#### Load
Replaces output db with latest aggregated results.

### Notes on code

#### Testing
Pytest suite exists and is run when the container spins up. As a time-saving choice I tested functionality that did fiddly stuff, which resulted in pretty low test coverage. Obviously in production this would be as high as possible.

#### Schema/QA
The checks I added with pandera also have really low coverage, but again a contributor could easily augment it.

#### Code quality
More time could have been devoted to type hints, exhaustive docstrings. I sacrificed this for speed.

#### Logging
Detailed logging of ETL runs would obviously be essential in production, however I sacrificed this for speed.  
