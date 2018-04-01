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

@app.route('/')
def homepage():
    """render the homepage.html template"""


    return render_template("/homepage.html")


@app.route('/top-melons')
def top_melons():
    """Return page showing the details of a given melon.

    Show all info about a melon.
    """

    
    melon_name = MOST_LOVED_MELONS[key]["name"]
    melon_loved = MOST_LOVED_MELONS[key]["num_loves"]
    melon_img = MOST_LOVED_MELONS[key]["img"]

    print melon_name
    return render_template("top-melons.html", melon_name=MOST_LOVED_MELONS[key]["name"], melon_loved=MOST_LOVED_MELONS[key]["num_loves"], melon_img=MOST_LOVED_MELONS[key]["img"])

@app.route('/get-name')
def get_name():
    """set user's name in session"""

    session["person"] = request.args.get("person")

    return redirect("/top-melons.html")

@app.route('/love-melon')
def love_melon():
    """will post request from top-melons"""

    return redirect("/love-melon")

if __name__ == "__main__":

    #TEST

    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
