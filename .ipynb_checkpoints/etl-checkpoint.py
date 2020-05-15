import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries

"""
Load data from S3 to staging tables on Redshift
"""
def load_staging_tables(cur, conn):
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()  
    print("Stage tables loaded.\n")

"""
Load data from staging tables analytics tables on Redshift
"""
def insert_tables(cur, conn):
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()
    print("insering tables done.\n")
"""
Connects to Sparkify redshift datase, loads log_data and song_data into the staging tables,
tranform into the five analytics tables.
"""
def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()