__author__ = 'hyeonsj'
import pymysql
import init


class Connect:

    conn = None
    cur = None

    def __init__(self):
        try:
            conn = pymysql.connect(host=init.host, user=init.user, passwd=init.passwd, db=init.db, charset=init.charset)
            self.conn = conn
            self.cur = conn.cursor()
        except pymysql.InternalError as error:
            code, message = error.args
            print(">>>>>>>>>>>>>", code, message)

    def get_cursor(self):
        return self.cur

    def find(self, sql):
        try:
            self.cur.execute(sql)
            return self.cur

        except pymysql.InternalError as error:
            code, message = error.args
            print(">>>>>>>>>>>>>", code, message)
            return code, message

    def insert(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()

            sql = "SELECT LAST_INSERT_ID();"
            self.cur.execute(sql)
            return self.cur

        except pymysql.InternalError as error:
            code, message = error.args
            print(">>>>>>>>>>>>>", code, message)
            return code, message

    def delete(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
            return self.cur

        except pymysql.InternalError as error:
            code, message = error.args
            print(">>>>>>>>>>>>>", code, message)
            return code, message

    def update(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
            return self.cur

        except pymysql.InternalError as error:
            code, message = error.args
            print(">>>>>>>>>>>>>", code, message)
            return code, message

    def close_db(self):
        try:
            self.cur.close()
            self.conn.close()
        except pymysql.InternalError as error:
            code, message = error.args
            print(">>>>>>>>>>>>>", code, message)