from flask import Flask, jsonify, make_response
import requests
import os
import simplejson as json

app = Flask(__name__)

database_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(database_path)


f = open("{}/database/users.json".format(database_path), 'r')
usr = json.load(f)


@app.route('/')
def hello():
    ''' Greet the user '''

    return "Hey! The service is up, how about doing something useful"


@app.route('/users')
def users():
    ''' list of users '''

    resp = make_response(json.dumps(usr, sort_keys=True, indent=4))
    resp.headers['Content-Type'] = "application/json"
    return resp


@app.route('/users/<username>')
def user_data(username):
    '''returns specified user'''

    if username not in usr:
        return 'not found'

    return jsonify(usr[username])


@app.route('/users/<username>/lists')
def user_lists(username):
    '''return list of users with username'''

    try:
        req = requests.get("http://127.0.0.1:5000/lists/{}".format(username))

    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return req.text


if __name__ == '__main__':
    app.run(port=5000, debug=True)

