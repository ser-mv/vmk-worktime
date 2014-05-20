import database_sql
import http_server
import api
import os
import urlparse

app = http_server.http_server

if __name__ == "__main__":
    db = database_sql.database_sql()
    db.init_sqlite('temp/db')
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
