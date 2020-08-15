#################################################
# Import
#################################################
# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Routes
#################################################
# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

#################################################
# Finish
#################################################
if __name__ == "__main__":
    app.run()
