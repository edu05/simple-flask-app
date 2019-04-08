from flask import Flask, render_template, request
import logging, json

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

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

@flask_app.route('/')
def location_browser():
    # Read hardcoded locations
    with open('NamLocRev.json') as json_file:
        locations = byteify(json.load(json_file))
        print type(locations)
        return render_template("index.html", locations=locations)


@flask_app.route('/add-location', methods=['POST', 'GET'])
def add_location():
    if request.method == 'POST':
        with open('NamLocRev.json') as json_file:
            new_loc = request.form.get('new_location') # loc from client saved onto variable; type: unicode
            new_loc = byteify(new_loc) # type:str
            location_dict = {'name': new_loc}
            print location_dict # holds a dict
            json_data = json.load(json_file)
            print json_data
            entry = {'name': new_loc, 'description': '', 'photo_url': '', 'position': [], 'review': [{'text': '', 'author': '', 'mark': ''}]}
            json_data.append(entry)
            with open('NamLocRev.json', 'w') as file:
                file.write(json.dumps(json_data))
            return render_template("index.html")
    return render_template("add-location.html")


@flask_app.route('/about')
def about_page():
    return render_template("about.html")




logger.info('STARTING APP, TRY IT OUT!!!')

if __name__ == '__main__':
    flask_app.run(debug=True, use_reloader=True)
