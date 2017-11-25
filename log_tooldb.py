import psycopg2

# Sets up databe connection


def connect(dbname="news"):
    try:
        db = psycopg2.connect(dbname=dbname)
        c = db.cursor()
        return db, c
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# Retrieve articles ordered by most views


def get_articles():
    db, c = connect()
    query = """SELECT art.title, count(*) article_views
        FROM authors aut, articles art, log l
        WHERE aut.id = art.author and l.path = '/article/' || art.slug
        GROUP BY art.title
        ORDER BY article_views DESC
        LIMIT 3;"""
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results

# Retrieve authors ordered by most views


def get_authors():
    db, c = connect()
    query = """SELECT aut.name, count(*) article_views
        FROM authors aut, articles art, log l
        WHERE aut.id = art.author and l.path = '/article/' || art.slug
        GROUP BY aut.name, l.status
        ORDER BY article_views DESC;"""
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results

# Retrieve log data grouped by status, ordered by most views


def get_access_logs():
    db, c = connect()
    query = """SELECT TOTAL.date, TOTAL.num, ERROR.num, 
    (ERROR.num::decimal/TOTAL.num::decimal) * 100 AS average FROM
    (SELECT to_char(date(time), 'YYYY-MM-DD') date, count(*) num
    FROM log
    GROUP BY date
    ORDER BY date ASC) AS TOTAL,
    (SELECT to_char(date(time), 'YYYY-MM-DD') date, count(*) num
    FROM log
    WHERE status = '404 NOT FOUND'
    GROUP BY status, date
    ORDER BY date ASC) AS ERROR
    WHERE TOTAL.date = ERROR.date
    GROUP BY TOTAL.date, TOTAL.num, ERROR.num
    ORDER BY TOTAL.date ASC;"""
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results
