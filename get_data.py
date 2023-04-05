from config import config
import psycopg2
import argparse


def get_data(table_name):
    cmd = "SELECT * FROM {} ORDER BY id".format(table_name)
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(cmd)

        print('Total Number of data:', cur.rowcount)
        # row = cur.fetchone()
        # while row is not None:
        #     print(row)
        #     row = cur.fetchone()
        rows = cur.fetchall()
        
        for row in rows:
            print(row)
        cur.close()

    except (Exception, psycopg2.DatabaseError) as e:
        print(e)

    finally:
        if conn is not None:
            conn.close()



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Enter Table Name")
    parser.add_argument('table_name', help="Table Name")
    args = parser.parse_args()
    get_data(args.table_name)
