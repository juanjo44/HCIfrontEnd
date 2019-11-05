import pymysql
from db_config import mysql

class MoviesRepository(object):
    def __init__(self):
        self.conn = mysql.connect()

    def add_movie(self, name):
        sql = "INSERT INTO movies(name,description,stars,year) VALUES(%s,%s,%d,%d)"
        data = (name,description,stars,year,)
        cursor = self.conn.cursor()
        cursor.execute(sql, data)
        self.conn.commit()
        lastrowid = cursor.lastrowid
        cursor.close()
        return lastrowid

    def get_all_movie(self, page, pagesize, name):
        print("...repo....name: " +name)
        startat = page*pagesize
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        if name:
            cursor.execute("SELECT id, name, description FROM movies WHERE name LIKE %s LIMIT %s, %s", (name,startat, pagesize))
        else:
            cursor.execute("SELECT id, name, description FROM movies LIMIT %s, %s", (startat, pagesize))

        rows = cursor.fetchall()
        cursor.close()
        return rows

    def get_movie_by_id(self, id):
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, name, description FROM movies WHERE id=%d", id)
        row = cursor.fetchone()
        cursor.close()
        return row

    def update_movie(self, id, name, description):
        sql = "UPDATE movies SET name=%s,description=%s WHERE id=%d"
        data = (name,description, id,)
        cursor = self.conn.cursor()
        rows_affected = cursor.execute(sql, data)
        self.conn.commit()
        cursor.close()
        return rows_affected

    def delete_movie(self, id):
        cursor = self.conn.cursor()
        rows_affected = cursor.execute("DELETE FROM movies WHERE id=%d", (id,))
        self.conn.commit()
        cursor.close()
        return rows_affected