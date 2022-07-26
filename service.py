from flask import Flask, render_template, request
import query_manager as query
import json
import pprint

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('/index.html', test="uueueueue")

@app.route("/query/find_by_name", methods=['POST'])
def find_by_name():
    if request.method == 'POST':
        name = request.form['name']
        results = query.find_game_by_name(name)
        pprint.pprint(results)
        return render_template('/query.html', results=results, size=len(results), title="Ricerca per nome: "+name)
    return json.dumps({"ok":True})

@app.route("/query/find_by_category", methods=['POST'])
def find_by_category():
    if request.method == 'POST':
        category = request.form['category']
        results = query.find_game_by_category(category)
        pprint.pprint(results)
        return render_template('/query.html', results=results, size=len(results), title="Ricerca per categoria: "+category)
    return json.dumps({"ok":True})


@app.route("/query/find_by_review_count", methods=['POST'])
def find_by_review_count():
    if request.method == 'POST':
        count = request.form['count']
        results = query.find_game_by_review_count(count)
        pprint.pprint(results)
        return render_template('/query.html', results=results, size=len(results), title="Ricerca con numero recensioni maggiore di: "+count)
    return json.dumps({"ok":True})


@app.route("/query/find_by_review_rating", methods=['POST'])
def find_by_review_rating():
    if request.method == 'POST':
        rating = request.form['rating']
        results = query.find_game_by_review_rating(rating)
        pprint.pprint(results)
        return render_template('/query.html', results=results, size=len(results), title="Ricerca con rating recensione maggiore di: "+rating)
    return json.dumps({"ok":True})

@app.route("/query/find_orderby_price", methods=['POST'])
def find_orderby_price():
    results = query.find_game_orderby_price()
    pprint.pprint(results)
    return render_template('/query.html', results=results, size=len(results), title="Ricerca ordinata per prezzo")

@app.route("/query/find_orderby_rating", methods=['POST'])
def find_orderby_rating():
    results = query.find_game_orderby_rating()
    pprint.pprint(results)
    return render_template('/query.html', results=results, size=len(results), title="Ricerca ordinata per rating")


app.run(port=5005)