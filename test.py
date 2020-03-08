from flask import Flask, request
from SearchEngine import *
import base64

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET', 'POST'])
def feedback():
    """
    ...
    """
    if request.method == 'POST':
        req_data = request.get_json()
        if not req_data:
            return json.dumps({'bool': True, 'violation': []})
        img = req_data['captures']
        imgdata = base64.b64decode(img)
        file_name = 'downloaded_image.jpg'
        with open(file_name, 'wb') as f:
            f.write(imgdata)
        preference = req_data['pref']
        to_ret = {'bool': True, 'violation': []}
        for pref in preference:
            search_engine = InputData(file_name)
            to_ret = search_engine.is_ok(pref)
            if not to_ret['bool']:
                to_ret = json.dumps(to_ret)
                return to_ret
        to_ret = json.dumps(to_ret)
        return to_ret
    else:
        return json.dumps({'bool': True, 'violation': []})


app.run(host='127.0.0.1')
