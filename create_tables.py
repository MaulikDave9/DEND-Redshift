import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


"""
Drop existing tables from sparkify database
cur: connect to DB, execute SQL commands
conn: connection to DB
Executes SQL DROP tables in the beginning if the tables already exist.
That way, running this script(create_tables.py) to reset the database and test ETL pipeline.
"""
def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

"""
Create tables - 
staging tables: staging_events, staging_songs
analytics tables: songplays, users, songs, artists, time
"""
def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()
        
        
"""
Connect to Redshift (Amazon Cloud DWH), create new DB, drop and create tables.
"""

def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
    
    # Load Parameters from the config file.
    KEY                = config.get('AWS','KEY')
    SECRET             = config.get('AWS','SECRET')

    HOST               = config.get("CLUSTER","HOST")
    DB_NAME            = config.get("CLUSTER","DB_NAME")
    DB_USER            = config.get("CLUSTER","DB_USER")
    DB_PASSWORD        = config.get("CLUSTER","DB_PASSWORD")
    DB_PORT            = config.get("CLUSTER","DB_PORT")

    ARN                = config.get("IAM_ROLE", "ARN")

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()

if __name__ == "__main__":
    main()