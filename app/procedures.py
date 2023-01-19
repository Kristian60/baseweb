import sqlite3
import os

def call_db(query):
    sqliteConnection = sqlite3.connect('app/db/db.db')
    cursor = sqliteConnection.cursor()

    cursor.execute(query)
    record = cursor.fetchall()
    cursor.close()
    return record


def get_top_worldwide(gender):
    query = f'''
    select * from athletes a

    join skills s
    on a.athlete_id = s.athlete_id
    where a.gender = '{gender}'
    and to_date = '9999-12-31'
    
    order by mu-3*sigma desc
    
    LIMIT 10;
    '''

    return call_db(query)[:10]

def get_top_per_nationality(nation, gender):
    query = f'''
    select * from athletes a

    join skills s
    on a.athlete_id = s.athlete_id
    
    where a.gender = '{gender}'
    and a.nationality = '{nation}'
    and to_date = '9999-12-31'
    
    LIMIT 10;
    '''

    return call_db(query)[:10]


if __name__ == '__main__':
    f = get_top_per_nationality('DK','M')

    print('ok')
