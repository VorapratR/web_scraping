import flask
from flask import request, jsonify

from web_scraping import ml_model, web_scraping

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def api():
    base_res = {
        'result': 1,
        'detail': '',
        'message': 'Success'
    }
    return jsonify(base_res)


@app.route('/investing', methods=['GET'])
def api_all():
    equities = request.args.get('equities', default='*', type=str)
    if(equities):
        base_res = {
            'result': 1,
            'detail': ml_model(web_scraping(equities)),
            'message': 'Success'
        }
    else:
        base_res = {
            'result': 0,
            'detail': '',
            'message': 'Equities is null'
        }
    return jsonify(base_res)


app.run()
