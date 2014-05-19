import database_sqlite
import http_server
import api

app = http_server.http_server

if __name__ == "__main__":
    db = database_sqlite.database_sqlite('temp/db')
    http_server.website.db = db
    api.db = db
    app.run(host = '0.0.0.0')
else:
    db = database_sqlite.database_sqlite('temp/db2')
    http_server.website.db = db
    api.db = db
