import database_sql
import http_server
import api
import os
import urlparse

app = http_server.http_server

if __name__ == "__main__":
    urlparse.uses_netloc.append("postgres")
    url = urlparse.urlparse('postgres://otetypapzlkjgi:SEEUIn461F_V5YgnN-Whx0NJpC@ec2-54-225-182-133.compute-1.amazonaws.com:5432/dcgu94mppt32j1')
    db = database_sql.database_sql()
    db.init_postgresql(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )

    #db = database_sql.database_sql()
    #db.init_sqlite('temp/db')
    http_server.website.db = db
    api.db = db
    app.run(host = '0.0.0.0')
else:
    #heroku config:
    urlparse.uses_netloc.append("postgres")
    url = urlparse.urlparse(os.environ["DATABASE_URL"])
    db = database_sql.database_sql()
    db.init_postgresql(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
    http_server.website.db = db
    api.db = db
