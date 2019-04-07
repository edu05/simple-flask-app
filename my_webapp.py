from flask import Flask, render_template
import logging
import json

flask_app = Flask(__name__)

#CONFIGURING LOGGING
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

fh = logging.FileHandler('application_logs.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)

@flask_app.route('/')
def homepage():
    return render_template("index.html")

@flask_app.route('/locations')
def location_browser():
    # Read hardcoded locations
    with open('NamLocRev.json') as json_file:
        locations = json.load(json_file)
        return render_template("locationBrowser.html", locations=locations)

@flask_app.route('/about')
def aboutpage():
    return render_template("about.html")


logger.info('STARTING APP, TRY IT OUT!!!')

if __name__ == '__main__':
    flask_app.run(debug=True, use_reloader=True)
