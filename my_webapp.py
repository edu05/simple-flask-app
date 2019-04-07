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

@flask_app.route('/jobs.html')
def jobs():
    return render_template("jobs.html")

@flask_app.route("/<name>")
def hello_someone(name):
    return render_template("hello.html", name=name.title())

logger.info('STARTING APP, TRY IT OUT!!!')

if __name__ == '__main__':
    flask_app.run(debug=True, use_reloader=True)



import requests

sender = ["Creative Aspirations"]
domain_name = "sandboxb49a93eedf4144a9ac2ed0a12ed78f79.mailgun.org"
api_key = "e201eb040a4d63c5f95987aa75ae992a-de7062c6-3b003f5d"
email_address = request.forms.get('recipient')

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/{0}/messages".format(domain_name),
        auth=("api", api_key),
        data={
            "from": "{0} <{0}@{1}>".format(sender[1], domain_name),
            "to": "{0}".format(email_address),
            "subject": "Thanks for signing up!",
            "text": "Thanks for signing up to Creative Aspirations! We'll be sure to keep you updated according to your preferences."
            }
        )

response = send_simple_message()

print response.url
print response.status_code
print response.headers["content-type"]
print response.text
