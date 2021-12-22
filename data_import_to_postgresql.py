import psycopg2


def copy_data_to_postgres():    
    copy_from_name_basics()
    copy_from_title_akas()
    copy_from_title_basics()
    copy_from_title_crew()
    copy_from_title_episode()
    copy_from_title_principals()
    copy_from_title_ratings()


def copy_from_name_basics():
    conn = psycopg2.connect("host=localhost dbname=imdb_db user=postgres password=123")
    cur = conn.cursor()
    with open('./data/name.basics.tsv', 'r') as f:
        next(f)
        cur.copy_from(f, 'name_basics', sep='\t')
        print("name_basics table is updated")
    conn.commit()

def copy_from_title_akas():
    conn = psycopg2.connect("host=localhost dbname=imdb_db user=postgres password=123")
    cur = conn.cursor()
    with open('./data/title.akas.tsv', 'r') as f:
        next(f)
        cur.copy_from(f, 'title_akas', sep='\t')
        print("title_akas table is updated")
    conn.commit()

def copy_from_title_basics():
    conn = psycopg2.connect("host=localhost dbname=imdb_db user=postgres password=123")
    cur = conn.cursor()
    with open('./data/title.basics.tsv', 'r') as f:
        next(f)
        cur.copy_from(f, 'title_basics', sep='\t')
        print("title_basics table is updated")
    conn.commit()

def copy_from_title_crew():
    conn = psycopg2.connect("host=localhost dbname=imdb_db user=postgres password=123")
    cur = conn.cursor()
    with open('./data/title.crew.tsv', 'r') as f:
        next(f)
        cur.copy_from(f, 'title_crew', sep='\t')
        print("title_crew table is updated")
    conn.commit()

def copy_from_title_episode():
    conn = psycopg2.connect("host=localhost dbname=imdb_db user=postgres password=123")
    cur = conn.cursor()
    with open('./data/title.episode.tsv', 'r') as f:
        next(f)
        cur.copy_from(f, 'title_episode', sep='\t')
        print("title_episode table is updated")
    conn.commit()

def copy_from_title_principals():
    conn = psycopg2.connect("host=localhost dbname=imdb_db user=postgres password=123")
    cur = conn.cursor()
    with open('./data/title.principals.tsv', 'r') as f:
        next(f)
        cur.copy_from(f, 'title_principals', sep='\t')
        print("title_principals table is updated")
    conn.commit()

def copy_from_title_ratings():
    conn = psycopg2.connect("host=localhost dbname=imdb_db user=postgres password=123")
    cur = conn.cursor()
    with open('./data/title.ratings.tsv', 'r') as f:
        next(f)
        cur.copy_from(f, 'title_ratings', sep='\t')
        print("title_ratings table is updated")
    conn.commit()