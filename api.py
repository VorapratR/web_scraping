import flask
from flask import request, jsonify

from web_scraping import ml_model, investing_scraping

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def api():
    response = {
        'result': 1,
        'detail': '',
        'message': 'Success'
    }
    return jsonify(response)


@app.route('/api/investing', methods=['GET'])
def api_investing():
    equities = request.args.get('equities', type=str)
    if(equities != None):
        equity = investing_scraping(equities)
        if equity != None:
            response = {
                'result': 1,
                'detail': ml_model(equity),
                'message': 'Success'
            }
        else:
            response = {
                'result': 0,
                'detail': ml_model(),
                'message': 'Error in investing_scraping'
            }
    else:
        response = {
            'result': 0,
            'detail': '',
            'message': 'Please add equities!'
        }
    return jsonify(response)


app.run()
