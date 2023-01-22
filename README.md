# cable-task

## Requirements

A working docker installation

## How to run

`cd cable-task` and `docker-compose up`. This will run `etl/run_end_to_end.sh`, which:
1. Runs the test suite
2. Runs the etl code 
3. Runs the script querying the final output db

## Other info

This repo contains a short sample of the data supplied, so the repo is lightweight but still keeps everything coupled together. This is completely seperate choice to the issue of processing chunks of data etc.! If you want to run on the full sample dataset, just `mv` the file into `cable-task/et/data/enhanced_synthetic_data_2.csv`.

## Notes on the dataset

### Data quality appears to be a significant issue:

From a quick look in excel:
* Time formats appear to be in stopwatch time, not clock time
* Lots of names corrupted
* Some email addresses contain whitespace
* Some phone numbers appear invalid
* DOB formats inconsistent
* Many users share same `customer` value, which is not necessarily an issue
* user_id unique?

### Data Governance
This dataset is full of personally identifiable info. That would obviously affect all decisions about where this pipeline moves data too, and indeed whether it could run at all. 


## Notes on the solution

### Notes on architecture
I wrote my solution to be easily adaptable to work with an external persistent db, which would make the following architecture work in production. Obviously at the moment it just interacts with the sqlite dbs in the repo.

1. pre-extract: incoming raw csv chunk pushed to db
2. extract: full dataset read from db
3. transform: data aggregated
4. load: transformed data pushed to db

#### Pre-extract
The idea of the pre-extract phase is to `append` incoming chunks of data to a datastore, which will be read in totality in the extract step. This was my interpretation of a pipeline that can handle data ingestion over time in production. Adding a field indicating date of ingestion adds some context to this raw data. I also chose to create the table with a primary key, which during my development made sense, but may not be necessary for this datastore.

#### Extract
Sends a `SELECT * ` query to the pre-extract db. Runs `pandera` schema checks - I just added one to validate the postcodes which are later used for the transformations. However this functionality could be easily expanded for a proper schema/QA step.

#### Transform
Runs a function calculating the top 10 most common postcodes.

#### Load
Appends to output db

### Notes on code

#### Testing
Pytest suite exists and is run when the container spins up. As a time-saving choice I tested functionality that did fiddly stuff, which resulted in pretty low test coverage. Obviously in production this would be as high as possible.

#### Schema/QA
The checks I added with pandera also have really low coverage, but again a contributor could easily augment it.

#### Code quality
More time could have been devoted to type hints, exhaustive docstrings. I sacrificed this for speed.

