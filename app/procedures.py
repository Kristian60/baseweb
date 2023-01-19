import sqlite3
import os

def call_db(query):
    print(os.getcwd())
    sqliteConnection = sqlite3.connect('app/db/db.db')
    cursor = sqliteConnection.cursor()

    cursor.execute(query)
    record = cursor.fetchall()
    cursor.close()
    return record


def get_top_worldwide(gender):
    query = f'''
    select * from athletes a

    where a.gender = '{gender}'
    order by RANDOM()
    '''

    return call_db(query)[:10]

def get_top_per_nationality(nation, gender):
    query = f'''
    select * from athletes a

    where a.nationality = '{nation}'
    and a.gender = '{gender}'
    order by RANDOM()
    '''

    return call_db(query)[:10]


if __name__ == '__main__':
    f = get_top_per_nationality('DK','M')

    print('ok')
