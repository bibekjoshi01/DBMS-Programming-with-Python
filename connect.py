import psycopg2
from config import config

def connect():
    '''Connect to the postgreSql server'''
    conn = None

    try:
        params = config()
        print('connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # excute a statement
        cur.execute('SELECT version()')
        db_version = cur.fetchone()

        print('----------------------------------------------------')
        print('| PostgreSQL database Version')                      
        print("|", db_version)
        print('----------------------------------------------------')

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed')
    

if __name__ == '__main__':
    connect()

