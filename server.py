import flask
app = flask.Flask("max-mine.ru", template_folder="pages")


@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/docs")
def docs():
    return flask.render_template("docs.html")

@app.route("/pkg/<path:filename>")
def pkg(packagename):
    return flask.send_from_directory("pkg", packagename)

@app.route("/files/<path:filename>")
def files(filename):
    return flask.send_from_directory("files", filename)

app.run("0.0.0.0", 5001)