from mysql.connector  import connect  # pip install mysql-connector-python
from customermodel import Customer
import json

def get_connection():
    try:
        with open('config.json') as fp:
            config = json.load(fp)
            return connect(**config)
    except Exception:
        print('Something went wrong and cannot go any further.')
        exit(1)

def get_all_customers():
    sql = 'select id, name, city, email from CUSTOMERS'
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            customers = []
            for each_rec in cur.fetchall():
                c = Customer()
                c.id = each_rec[0]
                c.name = each_rec[1]
                c.city = each_rec[2]
                c.email = each_rec[3]
                customers.append(c)

            return customers
        
def add_new_customer(cust: Customer):
    sql = 'insert into CUSTOMERS (name, city, email) values (%s, %s, %s)'
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (cust.name, cust.city, cust.email))
            cust.id = cur.lastrowid
            conn.commit()
            return cust

def get_one_customer(cust_id:int):
    sql='select id, name, city, email from CUSTOMERS where id=%s'
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql,(cust_id,))
            rec=cur.fetchone()
            if rec is None:
                return None
            c=Customer()
            c.id=rec[0]
            c.name=rec[1]
            c.city=rec[2]
            c.email=rec[3]
            return c