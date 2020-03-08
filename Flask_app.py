from ImageLoader import *
from RealImageLoader import *
from SearchEngine import *
from User import *
from flask import Flask
from flask import request, jsonify
import json
app = Flask(__name__)

CLOUD_STORAGE = '/users/vikagerman/Desktop/hackathon'

# We create a dictionary (similar to a JSON) which contains data that our app will use
# Below is an example of the format of a python Dictionary/JSON
'''
[
    {'id':0,
     'name': 'Vriska Serket',
     'alignment': 'Chaotic Good',
     'star_sign': 'Scorpio'
    },
    {'id':1,
     'name': 'Karkat Vantas',
     'alignment': 'Lawful Good',
     'star_sign': 'Cancer'
    },
    {'id':2,
     'name': 'Nepeta Leijon',
     'alignment': 'Chaotic Cat',
     'star_sign': 'Leo'
    }
]
'''
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/random', methods = ['GET'])
def json_return():
    with open('Database.json', 'r') as filename:
        j = filename.read()
        filename.close()
    return jsonify(j)

@app.route('/one', methods=['POST', 'GET'])
def image_transport():
    '''
    if request.method == 'POST':
        
    '''
    if request.method == 'POST':
            # check if the post request has the file part
            # data = request.args.get()
            # preferences = data['preferences']            
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                # file.save(os.path.join(app.config['CLOUD_STORAGE'], filename))
                ss = InputData(filename)
@app.route('/anything', methods=['POST', 'GET'])
def fin ():
    if request.method == 'POST':
        data = request.args()
        #assume that the dictionary is in form {?preferences=one,two,three;image=big_big_string}
        preferences = data['preferences']
        image = data[image][0]
        obj = InputData(filename)
        value = obj.is_ok(preferences)
        return value

app.run(host='0.0.0.0')
