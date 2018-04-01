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
from flask import render_template
# YOUR ROUTES GO HERE


@app.route("/", methods=["GET"])
def homepage():
    """render the homepage.html template. Button redirects user to get-name.html"""
    person=request.args.get("person")

    if session["person"]:
        return redirect("/top-melons")
    # elif session["person"] == None:
    #     return render_template('/get-name.html')
    else:
        return render_template("/homepage.html")

@app.route("/get-name", methods=["GET", "POST"])
def get_name():
    """set user's name. Button redirects user to top-melons.html"""
    person=request.args.get("person")

    if session["person"]:
        return redirect("/top-melons")
    else:
        return redirect("/get-name")


@app.route("/top-melons", methods=["GET", "POST"])
def top_melons():
    """Return page showing the details of a given melon.

    Show all info about a melon.
    """
    for key in MOST_LOVED_MELONS:
        melon_name = MOST_LOVED_MELONS[key]["name"]
        melon_loved = MOST_LOVED_MELONS[key]["num_loves"]
        melon_img = MOST_LOVED_MELONS[key]["img"]
        person = request.args.get("person")

    if person or session["person"]:
        return render_template("top-melons.html", 
            person=request.args.get("person"),
            melon_name=MOST_LOVED_MELONS[key]["name"], 
            melon_loved=MOST_LOVED_MELONS[key]["num_loves"], 
            melon_img=MOST_LOVED_MELONS[key]["img"])
    else:
        person="Good-looking"
        return render_template("top-melons.html", 
            person=request.args.get("person"),
            melon_name=MOST_LOVED_MELONS[key]["name"], 
            melon_loved=MOST_LOVED_MELONS[key]["num_loves"], 
            melon_img=MOST_LOVED_MELONS[key]["img"])

    
@app.route("/thank-you")
def thank_you():
    """Return thank-you.html for visiting Ubermelon"""

    return render_template("/thank-you.html")

if __name__ == "__main__":

    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
