import psycopg2
from config import config

def update_vendor(vendor_id, vendor_name):
    '''Upadate Vendor name based on vendor id'''
    cmd = """UPDATE vendors SET vendor_name = %s WHERE vendor_id = %s"""

    conn = None
    updated_rows = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Getting initial name
        cur.execute("""SELECT vendor_name FROM vendors WHERE vendor_id = %s""", (vendor_id,))
        row = cur.fetchone()
        initial_name = row[0]

        cur.execute(cmd, (vendor_name, vendor_id))

        updated_rows = cur.rowcount

        conn.commit()
        cur.close()

        print("{} Updated to {} Successfully !".format(initial_name, vendor_name))

    except (Exception, psycopg2.DatabaseError) as e:
        print(e)
    
    finally:
        if conn is not None:
            conn.close()
    
    return updated_rows


if __name__ == '__main__':
    # Update vendor id 1
    update_vendor(1, "Dibya Panday")