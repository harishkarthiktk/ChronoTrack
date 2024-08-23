from flask import Flask
from flask import render_template

import DBModel

app = Flask(__name__)


# ------------------
## following routes are for page routes 

@app.route("/<catch_all>")
def hello(catch_all):
    return render_template("page_not_found.html", title="Page Not Found")

@app.route("/app")
@app.route("/") 
@app.route("/app/table")
def table_copy():
    items = DBModel.get_all_watercans()
    print(items)
    return render_template("table.html", title="App Page", items = items)

# ------------------
## following routes are for apis

@app.route("/api/watercans/")
def watercans():
    watercans = DBModel.get_all_watercans()

    return watercans

app.run(host="0.0.0.0", port=8080, debug=True)