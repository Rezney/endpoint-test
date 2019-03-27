import json
import flask
from flask import jsonify, request
from urllib.parse import urljoin

app = flask.Flask(__name__)
app.config["DEBUG"] = True

AGREEMENT_STR = 'I agree that I will be cool!'
APP_URL_PREFIX = '/r/insights/platform/leapp/'

with open('test.json', 'r') as fo:
    reports = json.load(fo)

@app.route(urljoin(APP_URL_PREFIX, 'test'), methods=['POST'])
def get_reports():
    req = request.get_json()
    agreement = None
    if 'agreement' in req:
        agreement = req_data['agreement']
        if agreement == AGREEMENT_STR:
            return jsonify(reports)
    else:
        return "Madafaka"


if __name__ == '__main__':
    application.run()

