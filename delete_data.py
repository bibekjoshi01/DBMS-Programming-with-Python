import psycopg2
from config import config
import argparse


def delete_data(table_name, id):
    '''Delete table data based on id'''

    cmd = "DELETE FROM {} WHERE id = {}".format(table_name, id)

    conn = None
    deleted_rows = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("SELECT * FROM {} WHERE id = %s".format(table_name), (id,))
        row = cur.fetchone()
        if row is not None:
            deleted_id = row[0]
        else:
            print("No row found with id:", id)
            exit()

        # Transactions using the with statement
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute(cmd)

        deleted_rows = cur.rowcount
        conn.commit()
        cur.close()

        print("-------------------------------------------------")
        print("|", deleted_rows, "data deleted !")
        print("| {} having id={} Deleted Successfully !".format(table_name, deleted_id))
        print("-------------------------------------------------")

    except (Exception, psycopg2.DatabaseError) as e:    
        print(e)
    
    finally:
        if conn is not None:
            conn.close()
    
    return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('table_name', help="Table Name")
    parser.add_argument('id', help="Table Name")
    args = parser.parse_args()
    delete_data(args.table_name, args.id)
