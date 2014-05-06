import database_sqlite
import http_server

if __name__ == "__main__":
    db = database_sqlite.database_sqlite('temp/db')
    http_server.website.db = db
    http_server.http_server.run(host = '0.0.0.0')
