

from flask import Flask, request
import website_authorization
import website

app = Flask(__name__)



def requires_auth(f):
    '''Enables authorization request'''
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or \
           not website_authorization.check_auth(auth.username, auth.password):
            return website_authorization.authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route("/")
#@requires_auth
def index_page():
    return website.index_page()




