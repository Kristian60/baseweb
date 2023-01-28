import sqlite3

def call_db(query):
    def name_items(x, names):
        return {q:z for q,z in zip(names, x)}

    sqliteConnection = sqlite3.connect('app/db/db.db')
    cursor = sqliteConnection.cursor()

    values = cursor.execute(query)
    col_name_list = [tuple[0] for tuple in values.description]
    record = cursor.fetchall()
    cursor.close()
    return [name_items(x,col_name_list) for x in record]


def get_top_worldwide(gender):
    query = f'''
    select * from athletes a

    join skills s
    on a.athlete_id = s.athlete_id
    where a.gender = '{gender}'
    and to_date = '9999-12-31'
    and model_id = 104
    
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
    and s.to_date = '9999-12-31'
    and model_id = 104
    
    order by mu-3*sigma desc
    
    LIMIT 10;
    '''

    return call_db(query)[:10]

def get_athlete_info(athlete_id):
    query = f'''
    select * from athletes a
    
    join countries c
    on c.country_iso = a.nationality
    
    where a.athlete_id = {athlete_id}
    '''

    return call_db(query)

def get_all_competitions(athlete):
    query = f'''
    select * from competitions c
    
    join placements p
    on p.comp_id = c.comp_id
    
    left join teams t
    on t.team_id = p.team_id
    
    left join athletes a1
    on a1.athlete_id = t.athlete_id
    
    left join athletes a2
    on a2.athlete_id = p.athlete_id
    
    where a1.athlete_id = {athlete} or a2.athlete_id = {athlete}
    
    order by c.date desc
    '''

    print(query)
    return call_db(query)

def get_teammates(tids):
    tstring = ','.join([str(x) for x in tids])
    query = f'''
    select * from teams t
    
    join athletes a
    on a.athlete_id = t.athlete_id
    
    where t.team_id in ({tstring})'''
    return call_db(query)


if __name__ == '__main__':
    p = get_all_competitions(3871)
    print('ok')