import pymysql
from db_config import mysql

class PersonRepository(object):
    def __init__(self):
        self.conn = mysql.connect()

    def add_person(self, name):
        sql = "INSERT INTO presons(name,phone,email) VALUES(%s,%s,%s)"
        data = (name,phone,email,)
        cursor = self.conn.cursor()
        cursor.execute(sql, data)
        self.conn.commit()
        lastrowid = cursor.lastrowid
        cursor.close()
        return lastrowid

    def get_all_person(self, page, pagesize, name):
        print("...repo....name: " +name)
        startat = page*pagesize
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        if name:
            cursor.execute("SELECT id, name FROM persons WHERE name LIKE %s LIMIT %s, %s", (name,startat, pagesize))
        else:
            cursor.execute("SELECT id, name FROM persons LIMIT %s, %s", (startat, pagesize))

        rows = cursor.fetchall()
        cursor.close()
        return rows

    def get_person_by_id(self, id):
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, name FROM persons WHERE id=%d", id)
        row = cursor.fetchone()
        cursor.close()
        return row

    def update_person(self, id, name):
        sql = "UPDATE persons SET name=%s WHERE id=%d"
        data = (name, id,)
        cursor = self.conn.cursor()
        rows_affected = cursor.execute(sql, data)
        self.conn.commit()
        cursor.close()
        return rows_affected

    def delete_person(self, id):
        cursor = self.conn.cursor()
        rows_affected = cursor.execute("DELETE FROM persons WHERE id=%d", (id,))
        self.conn.commit()
        cursor.close()
        return rows_affected