import pymysql
from db_config import mysql

class FullCastByMovieRepository(object):
    def __init__(self):
        self.conn = mysql.connect()

    def add_full_cast_by_movie(self, name):
        sql = "INSERT INTO full_cast_by_movie(id_person,id_role,id_movie,character) VALUES(%d,%d,%d,%s)"
        data = (id_person,id_role,id_movie,character,)
        cursor = self.conn.cursor()
        cursor.execute(sql, data)
        self.conn.commit()
        lastrowid = cursor.lastrowid
        cursor.close()
        return lastrowid

    def get_all_full_cast_by_movie(self, page, pagesize, id_movie):
        print("...repo....id_movie: " +id_movie)
        startat = page*pagesize
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        if name:
            cursor.execute("SELECT id_person, id_role, character FROM full_cast_by_movie WHERE id_movie LIKE %s LIMIT %s, %s", (id_movie,startat, pagesize))
        else:
            cursor.execute("SELECT id_person, id_role, character FROM full_cast_by_movie LIMIT %s, %s", (startat, pagesize))

        rows = cursor.fetchall()
        cursor.close()
        return rows

    def get_full_cast_by_movie_by_id_movie(self, id_movie):
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT character FROM full_cast_by_movie WHERE id_movie=%d", id)
        row = cursor.fetchone()
        cursor.close()
        return row

    def update_full_cast_by_movie(self, id_movie, character):
        sql = "UPDATE full_cast_by_movie SET character=%s WHERE id_movie=%d"
        data = (id_movie, character,)
        cursor = self.conn.cursor()
        rows_affected = cursor.execute(sql, data)
        self.conn.commit()
        cursor.close()
        return rows_affected

    def delete_full_cast_by_movie(self, id_movie):
        cursor = self.conn.cursor()
        rows_affected = cursor.execute("DELETE FROM full_cast_by_movie WHERE id_movie=%d", (id,))
        self.conn.commit()
        cursor.close()
        return rows_affected