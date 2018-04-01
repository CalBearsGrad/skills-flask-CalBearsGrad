from flask import Flask, redirect, request, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Getting our list of MOST LOVED MELONS
MOST_LOVED_MELONS = {
    'cren': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimRegular/crenshaw.jpg',
        'name': 'Crenshaw',
        'num_loves': 584,
    },
    'jubi': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Jubilee-Watermelon-web.jpg',
        'name': 'Jubilee Watermelon',
        'num_loves': 601,
    },
    'sugb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Sugar-Baby-Watermelon-web.jpg',
        'name': 'Sugar Baby Watermelon',
        'num_loves': 587,
    },
    'texb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Texas-Golden-2-Watermelon-web.jpg',
        'name': 'Texas Golden Watermelon',
        'num_loves': 598,
    },
}

# YOUR ROUTES GO HERE
from flask import render_template

@app.route("/", methods=["GET"])
def homepage():
    """render the homepage.html template"""
    if 'person' in session:
        print session
        print "You're one stepped closer to your most loved melon!"
        return redirect('/get-name')
    else:
        session['person'] = {}
        print session
        flash("You have successfully added your name!")
        return render_template('/get-name.html')

@app.route("/get-name", methods=["GET"])
def get_name():
    """set user's name in session"""

    session["person"] = request.args.get("person")

    return render_template("/get-name.html")


@app.route("/top-melons", methods=["POST"])
def top_melons():
    """Return page showing the details of a given melon.

    Show all info about a melon.
    """
    
    melon_name = MOST_LOVED_MELONS[key]["name"]
    melon_loved = MOST_LOVED_MELONS[key]["num_loves"]
    melon_img = MOST_LOVED_MELONS[key]["img"]
    person = session["person"]

    return render_template("top-melons.html", person=session["person"],melon_name=MOST_LOVED_MELONS[key]["name"], melon_loved=MOST_LOVED_MELONS[key]["num_loves"], melon_img=MOST_LOVED_MELONS[key]["img"])


@app.route("/love-melon")
def love_melon():
    """will post request from top-melons"""

    return redirect("/love-melon.html")

if __name__ == "__main__":

    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
