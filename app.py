from flask import Flask
import logging

app = Flask(__name__)

#CONFIGURING LOGGING
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

fh = logging.FileHandler('mylogs.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)



@app.route('/')
def homepage():
    return "Hello World"


logger.info('STARTING APP, TRY IT OUT!!!')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

