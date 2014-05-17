

from flask import Flask, request
import traceback
import json

import website_authorization
import website
import utils
import api

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

@http_server.route("/edit_employee", methods=['GET', 'POST'])
#@website_authorization.requires_auth
def edit_employee_page():
    employee_id = int(request.form.get('employee_id'))
    return website.edit_employee_page(employee_id)

@http_server.route("/new_employee", methods=['GET', 'POST'])
#@website_authorization.requires_auth
def new_employee_page():
    return website.edit_employee_page(-1, new_employee = True)

@http_server.route("/save_employee", methods=['GET', 'POST'])
#@website_authorization.requires_auth
def save_employee_page():
    return website.index_page(info_text = 'New employee successfully added')

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

    

@http_server.route("/add_working_seconds", methods=['POST'])
def add_working_seconds():
    try:
        employee_id = request.form.get('employee_id')
        password = request.form.get('password')
        working_seconds = request.form.get('working_seconds')
        return api.add_working_seconds(employee_id, working_seconds, password)
    except Exception, e:
        print traceback.format_exc()
        print e
