import psycopg2
from psycopg2 import sql
from psycopg2.extensions import DateFromPy
from pathlib import Path
import argparse

BASE_DIR = Path(__file__).resolve().parent

from config import config 


'''Insert Course Data'''

def insert_course(course_name):
    cmd = '''INSERT INTO course(name) VALUES(%s) RETURNING id;'''
    conn = None
    course_id = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(cmd, (course_name,))
        print(cur.rowcount)
        course_id = cur.fetchone()[0] 
        conn.commit()
        print(f"{course_name} added successfully ! id = {course_id}")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)

    finally:
        if conn is not None:
            conn.close()

    return None       


'''Insert Student Data'''

def insert_student(roll_no, full_name, age, dob, course):
    cmd = """
        INSERT INTO student(roll_no, full_name, age, dob, course_id) 
        VALUES (%s, %s, %s, %s, %s);
    """
    conn = None
    student_id = None
    records_to_insert = (roll_no, full_name, age, dob, course)
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(cmd, records_to_insert)
        student_id = cur.fetchone()[0]
        conn.commit()
        print(f"Student {full_name} added successfully ! id={student_id}")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()


'''Insert Teacher Data'''

def insert_teacher(full_name: str, qualification: str, course: int):
    cmd = """
        INSERT INTO teacher(full_name, qualification, course_id) VALUES ('bibek', 'MD', 9);
    """
    conn = None
    student_id = None
    records_to_insert = (full_name, qualification, course)
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        print(cmd)
        cur.execute(cmd)
        student_id = cur.fetchone()[0]
        conn.commit()
        print(f"Teacher {full_name} added successfully ! id={student_id}")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Insert Commands to insert data into tables")
    subparsers = parser.add_subparsers(dest="command")

    course_parser = subparsers.add_parser("course", help="Insert a new course")
    course_parser.add_argument("course_name", help="Name of the course")

    student_parser = subparsers.add_parser("student", help="Insert a new student")
    student_parser.add_argument("roll_no", help="Student roll number")
    student_parser.add_argument("full_name", help="Name of the student")
    student_parser.add_argument("age", help="Age of the student")
    student_parser.add_argument("dob", help="Date of birth of the student (YYYY-MM-DD)")
    student_parser.add_argument("course_id", help="Course ID of the student")

    teacher_parser = subparsers.add_parser("teacher", help="Insert a new teacher")
    teacher_parser.add_argument("full_name", help="Name of Teacher")
    teacher_parser.add_argument("qualification", help="Qualification")
    teacher_parser.add_argument("course_id", help="Course ID of the student")


    args = parser.parse_args()

    if args.command == "course":
        insert_course(args.course_name)
    elif args.command == "student":
        insert_student(args.roll_no, args.full_name, args.age, args.dob, args.course_id)
    elif args.command == "teacher":
        insert_teacher(args.full_name, args.qualification, args.course_id)
    else:
        print("Invalid Command")


# def insert_vendor_list(vendor_list):
#     """ insert multiple  into the vendors table  """
#     sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"
#     conn = None
#     try:
#         # read database configuration
#         params = config()
#         # connect to the PostgreSQL database
#         conn = psycopg2.connect(**params)
#         # create a new cursor
#         cur = conn.cursor()
#         # execute the INSERT statement
#         cur.executemany(sql,vendor_list)
#         # commit the changes to the database
#         conn.commit()
#         print("Data Inserted Successfully !")
#         # close communication with the database
#         cur.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()