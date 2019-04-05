from flask import Flask, render_template
import logging

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
    return render_template("Homepage.html")

@flask_app.route('/inspiration.html')
def inspiration():
    return render_template("inspiration.html")

@flask_app.route('/about_us.html')
def about_us():
    return render_template("about_us.html")

@flask_app.route(/"jobs.html")
def jobs():
    return render_template("jobs.html")

@flask_app.route("/<name>")
def hello_someone(name):
    return render_template("hello.html", name=name.title())

logger.info('STARTING APP, TRY IT OUT!!!')

if __name__ == '__main__':
    flask_app.run(debug=True, use_reloader=True)
