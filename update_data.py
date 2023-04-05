import psycopg2
from config import config
import argparse

def update_course(course_name, id):
    '''Upadate table data'''

    cmd = """UPDATE course SET name = %s WHERE id = %s"""

    conn = None
    updated_rows = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Getting initial name
        cur.execute("""SELECT name FROM course WHERE id = %s""", (id,))
        row = cur.fetchone()
        initial_name = row[0]

        cur.execute(cmd, (course_name, id))

        updated_rows = cur.rowcount

        conn.commit() 
        cur.close()

        print("{} Updated to {} Successfully !".format(initial_name, course_name))

    except (Exception, psycopg2.DatabaseError) as e:
        print(e)
    
    finally:
        if conn is not None:
            conn.close()
    
    return updated_rows


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('course_name', help="New Course Name")
    parser.add_argument('id', help='ID to update')
    args = parser.parse_args()
    update_course(args.course_name, args.id)

