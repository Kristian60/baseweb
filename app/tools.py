import psycopg2
import pandas as pd
import sqlite3

def gett(q):
    conn = psycopg2.connect(
        host="localhost",
        port=5433,
        database="postgres",
        user="postgres",
        password="walboGOLDa1p")
    cur = conn.cursor()
    cur.execute(q)
    colnames = [desc[0] for desc in cur.description]
    dat = cur.fetchall()

    e1 = [d for d in dat]
    out = []
    for e in e1:
        out.append({c: q for c, q in zip(colnames, e)})

    return out

def ps_to_sqlite():
    df = pd.DataFrame(gett('select * from dbo.skills'))
    df.to_csv('skills.csv', index=False)


if __name__ == '__main__':
    ps_to_sqlite()