import psycopg2

# Sets up database connection


def connect(dbname="news"):
    try:
        db = psycopg2.connect(dbname=dbname)
        c = db.cursor()
        return db, c
    except:
        print('Failed to connect to the database server.')

# Retrieve articles ordered by most views


def get_articles():
    db, c = connect()
    query = "select art.title, count(*) as article_views "
    query += "from public.authors as aut, public.articles as art, public.log as l "  # noqa
    query += "where aut.id = art.author and l.path like '/article/%'||art.slug "  # noqa
    query += "group by art.title "
    query += "order by article_views desc "
    query += "limit 3;"
    c.execute(query)
    return c.fetchall()
    db.close()

# Retrieve authors ordered by most views


def get_authors():
    db, c = connect()
    query = "select aut.name, count(*) as article_views "
    query += "from public.authors as aut, public.articles as art, public.log as l "  # noqa
    query += "where aut.id = art.author and l.path like '/article/%'||art.slug "  # noqa
    query += "group by aut.name, l.status "
    query += "order by article_views desc;"
    c.execute(query)
    return c.fetchall()
    db.close()

# Retrieve log data grouped by status, ordered by most views


def get_access_logs():
    db, c = connect()
    query = "SELECT OK.date, OK.num, ERROR.num FROM "
    query += "(SELECT to_char(date(time), 'YYYY-MM-DD') as date, count(*) as num "  # noqa
    query += "FROM public.log "
    query += "WHERE status = '200 OK' "
    query += "GROUP BY status, date "
    query += "ORDER BY date ASC) AS OK, "
    query += "(SELECT to_char(date(time), 'YYYY-MM-DD') as date, count(*) as num "  # noqa
    query += "FROM public.log "
    query += "WHERE status = '404 NOT FOUND' "
    query += "GROUP BY status, date "
    query += "ORDER BY date ASC) AS ERROR "
    query += "WHERE OK.date = ERROR.date "
    query += "GROUP BY OK.date, OK.num, ERROR.num "
    query += "ORDER BY OK.date ASC;"
    c.execute(query)
    return c.fetchall()
    db.close()
