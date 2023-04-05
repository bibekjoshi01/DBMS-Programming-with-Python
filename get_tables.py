import psycopg2
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

from config import config

def get_tables():
    conn = None
    command = """SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public'"""
    try:
        params = config()

        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(command)

        tables = [row[0] for row in cur.fetchall()]
        print("Tables:", tables)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as Error:
        print(Error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_tables()
