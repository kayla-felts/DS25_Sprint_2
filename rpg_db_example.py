"""An example of how to connect to a SQLite3 DB"""
import sqlite3
from query import GET_CHARACTERS


# Connects to db and creates cursor
def connect(db="rpg_db.sqlite3"):
    conn = sqlite3.connect(db)
    curs = conn.cursor()
    return conn, curs


# executes a sql query
def ex_q(curs, query):
    # temp_curs = conn.cursor()
    curs.execute(query)
    results = curs.fetchall()
    # temp_curs.close()
    return results


if __name__ == "__main__":
    rpg_conn, rpg_curs = connect()
    results = ex_q(rpg_curs, GET_CHARACTERS)
    print("This is the result: {}".format(results))
    rpg_curs.close()
