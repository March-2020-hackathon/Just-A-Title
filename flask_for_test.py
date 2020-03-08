from flask import Flask, request
from SearchEngine import *

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def feedback():
    """
    ...
    """
    req_data = request.get_json()
    if not req_data:
        return json.dumps({'bool': True, 'violation': []})
    img = req_data['captures'][0]
    preference = req_data['pref']
    to_ret = {'bool': True, 'violation': []}
    for pref in preference:
        search_engine = InputData(img)
        to_ret = search_engine.is_ok(pref)
        if not to_ret['bool']:
            to_ret = json.dumps(to_ret)
            return to_ret
    to_ret = json.dumps(to_ret)
    return to_ret


app.run(host='127.0.0.1')
