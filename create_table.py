import psycopg2
from config import config
from commands.crud_commands import CREATE_TABLE


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = CREATE_TABLE
    conn = None
    try:
        # read the connection parameters
        params = config()

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Executing commands
        for command in commands:
            cur.execute(command)

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()

        # print a success message
        print("Tables created successfully!")

    except (Exception, psycopg2.DatabaseError) as error:
        # rollback the transaction if an error occurs
        if conn is not None:
            conn.rollback()
        print(f"Error creating tables: {error}")

    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
