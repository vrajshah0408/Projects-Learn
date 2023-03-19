import flask

app = flask.Flask(__name__)


@app.route('/')
def firstpage():
    return flask.render_template("index.html")

@app.route('/info')
def infopage():
    return flask.render_template("info.html")

@app.route('/projects')
def projectpage():
    return flask.render_template("projects.html")    

app.run(debug=True)