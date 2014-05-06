

from flask import Flask, request
import traceback
import json

import website_authorization
import website
import utils


http_server = Flask(__name__, template_folder = 'html_templates', static_folder='')
http_server.debug = True




@http_server.route("/")
#@website_authorization.requires_auth
def index_page():
    return website.index_page()

@http_server.route("/image/<filename>")
def get_image(filename):
    print filename
    try:
        return http_server.send_static_file('img/' + filename)
    except Exception, e:
        print traceback.format_exc()
        print e

@http_server.route("/employees", methods=['GET', 'POST'])
#@website_authorization.requires_auth
def employees_page():
    try:
        filters = {}
        old_filters = request.form.get('old_filters')
        if old_filters:
            filters = json.loads(old_filters)
        new_filter_name = request.form.get('filter_name')
        new_filter_value = request.form.get('filter_value')
        if new_filter_name != None and new_filter_value != None:
            filters[new_filter_name] = new_filter_value
        month = request.form.get('month')
        if month == None:
            month = utils.current_month()
        sorting = request.form.get('sorting') or 1
        return website.employees_page(filters, month, sorting)
    except Exception, e:
        print traceback.format_exc()
        print e

    


