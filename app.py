from flask import Flask, request, render_template, redirect, jsonify, render_template_string
from flask_jsglue import JSGlue # this is use for url_for() working inside javascript which is help us to navigate the url
import util
import os
from werkzeug.utils import secure_filename

application = Flask(__name__)
application.debug = True

# JSGlue is use for url_for() working inside javascript which is help us to navigate the url
jsglue = JSGlue() # create a object of JsGlue
jsglue.init_app(application) # and assign the app as a init app to the instance of JsGlue

util.load_artifacts()
#home page
@application.route("/")
def home():
    return render_template("home.html")

#classify plant
@application.route("/classifyPlant", methods = ["POST"])
def classifyPlant():
    image_data = request.files["file"]
    #save the image to upload
    basepath = os.path.dirname(__file__)
    image_path = os.path.join(basepath, "uploads", secure_filename(image_data.filename))
    image_data.save(image_path)

    predicted_value, details = util.classify_plant(image_path)
    os.remove(image_path)
    return jsonify(predicted_value=predicted_value, details=render_template_string(details))


@application.route("/about")
def about():
    return render_template("about.html")

# here is route of 404 means page not found error
@application.errorhandler(404)
def page_not_found(e):
    # here i created my own 404 page which will be redirect when 404 error occured in this web app
    return render_template("404.html"), 404

if __name__ == "__main__":
    application.run()