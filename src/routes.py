from flask import current_app as app


# Flask routes go here

@app.route("/")
def test():
    return "Hello, world!"
