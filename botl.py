import bottle


@bottle.route("/")
def index():
    return "Hello Python!"


bottle.run(host="0.0.0.0", port=5000)
