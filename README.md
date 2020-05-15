# Project: Data Warehouse

## Description
Sparkify is a music streaming startup which has grown user base and song database.  
The data resides on S3 in the format of JSON logs and includes the user activity on the app
and metadata on the songs in the app.  This project builds an ETL pipeline to extrat the data from S3, 
stage in Redshift (Amazon cloud data warehouse) into set of dimentional tables.  This will enable
analytics team to query this tables and find the insight such as what songs users are interested in.  

## Database schema design 

### Fact Tables
        
    1. songplays - record in event data with songplays

### Dimension Tables

    2. users - users in the app
    3. songs - song in music database
    4. artists - artists in music database
    5. time - timestamps of records in songplays
    
    
### ETL pipeline

    1. Load data from S3 to staging tables on Redshift
    2. Load data from staging tables to analytics tables on Redshift


## Example queries

    1. Debugging in AWS Redshift Query Editor - after running create_table.py from the Project Workspace.
       Following query on each table was run to verify tables Schemas:
   
           select * from Information_schema.Columns WHERE table_name = 'staging_events'

    2. Analytic Tables can be leveraged to find insights very fast.
       Using query Editor in AWS Redshift console,
  
![query 1](images/query1.jpg)
   
![query 2](images/query2.jpg)
  
  
## Files

    (1) create_table.py: fact and dimension tables for the star schema in Redshift.

    (2) etl.py: load data from S3 into staging tables on Redshift and then process 
                that data into analytics tables on Redshift.

    (3) sql_queries.py: SQL statements to be imported into create_table.py and etl.py

## TO RUN

    (1) Create IAM User
            a. Create IAM Role with read access to S3
            b. Launch Redshift cluster
    
    (2) Fill out the details in dwh.cfg. 
    
            a. AWS Credentials - key, secret
            b. Cluster - hostname, database name, database user, database password
            c. IAM ROLE - ARN 
            d. S3 - paths for song and log data.
    
    (3) Run create_tables.py and etl.py python scripts in that order from the terminal

            root@16fb2f9e4347:/home/workspace# python create_tables.py
            root@16fb2f9e4347:/home/workspace# python etl.py