# Mock ETL pipeline from a streaming data source

Here we simulate a situation as follow: 
- __Data source A__ emits the streaming transactional data 
- We play the man in the middle to receive the data emitted by __A__ and ingest it into a postgreSQL instance as the target database/datawarehouse.

The __data source A__ is created as a mock API with Flask, and repeatedly send transactional data for every __t__ time (I hardcoded it at 0.01 seconds).
