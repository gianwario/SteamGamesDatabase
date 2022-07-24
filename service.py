from flask import Flask, render_template, request
import query_manager as query
import json

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('/index.html', test="uueueueue")

@app.route("/find_by_name", methods=['GET'])
def find_by_name():
    if request.method == 'GET':
        if("name" in request.args):
            name = request.args["name"]
            results = query.find_game_by_name(name)
            return json.dumps(results)
    return json.dumps({"ok":True})

app.run(port=5005)