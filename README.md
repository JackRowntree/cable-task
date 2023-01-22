# cable-task

## Requirements

A working docker installation

## How to run

`cd cable-task` and `docker-compose up`. This will run `etl/run_end_to_end.sh`, which:
1. Runs the test suite
2. Runs the etl code 
3. Runs the script querying the final output db

## Initial thoughts

#### Data quality appears to be a significant issue:

* Time formats appear to be in stopwatch time, not clock time
* Lots of names corrupted
* Some email addresses contain whitespace
* Some phone numbers appear invalid
* DOB formats inconsistent
* Many users share same `customer` value, which is not necessarily an issue
* user_id unique?

#### Data Governance
This dataset is full of personally identifiable info. That would obviously affect all decisions about where this pipeline moves data too, and indeed whether it could run at all. 


## Overall architecture:

1. pre-extract: incoming raw csv chunk pushed to db
2. extract: full dataset read from db
3. transform: data aggregated
4. load: transformed data pushed to db

# TODO
script checks
shoulds: 
QA checks, done
schemas, done
db upsert logic dnoe ish

