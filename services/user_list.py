from flask import Flask, jsonify
import os
import simplejson as json

app = Flask(__name__)

database_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

with open("{}/database/user_list.json".format(database_path), 'r') as j:
    usr_lst = json.load(j)


@app.route('/')
def hello():
    ''' Greet the user '''

    return "user_list service is up"


@app.route('/lists')
def show_lists():
    '''list of users'''

    lists = []

    for username in usr_lst:
        for user in usr_lst[username]:
            lists.append(user)
    return jsonify(lists)


@app.route('/lists/<username>')
def user_lists(username):

    if username not in usr_lst:
        return 'user not found'

    return jsonify(usr_lst[username])

if __name__ == '__main__':
    app.run(debug=True)
