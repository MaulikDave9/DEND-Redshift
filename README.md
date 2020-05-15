# Project: Data Warehouse

## Description
Sparkify is a music streaming startup which has grown user base and song database.  
The data resides on S3 in the format of JSON logs and includes the user activity on the app and metadata on the songs in the app.  
This project builds an ETL pipeline to extrat the data from S3, stage in Redshift (Amazon cloud data warehouse) into set of dimentional tables.  This will enable analytics team to query this tables and find the insight such as what songs users are interested in.  

## Database schema design and ETL pipeline

    1. Fact and dimension tables
    
     ![event datafile new Image](images/log-data.png)
    
    
    2. Redshift cluster, IAM Role
    3. ETL pipeline
        a. Load data from S3 to staging tables on Redshift
        b. Load data from staging tables to analytics tables on Redshift


## Example queries

1. Debugging in AWS Redshift Query Editor - after running create_table.py from the Project Workspace.
   Following query on each table was run to verify tables Schemas:
   
   select * from Information_schema.Columns WHERE table_name = 'staging_events'

2. Analytic Tables can be leveraged to find insights very fast:
   Using query Editor in AWS Redshift console,
   
   ![Query 2] (images/Query2.png)
   
## Files

(1) create_table.py: fact and dimension tables for the star schema in Redshift.
(2) etl.py: load data from S3 into staging tables on Redshift and then process that data into analytics tables on Redshift.
(3) sql_queries.py: SQL statements to be imported into create_table.py and etl.py

## TO RUN

(1) Fill out the details in dwh.cfg
(2) Run create_tables.py and etl.py python scripts in that order from the terminal

    root@16fb2f9e4347:/home/workspace# python create_tables.py
    root@16fb2f9e4347:/home/workspace# python etl.py