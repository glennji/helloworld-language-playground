from flask import Flask, jsonify
from dash_api import mock_responses as mock

api_version = "v1"

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, fools!"

@app.route('/v1/collections', methods=['GET'])
def get_collection_list():
    return jsonify(mock.collections)

@app.route('/v1/collections/<int:collection_id>', methods=['GET'])
def get_collection(collection_id):
    return jsonify(mock.collection)

@app.route('/%s/datasets' % api_version, methods=['GET'])
def get_dataset_list():
    return jsonify(mock.datasets)

@app.route('/%s/datasets/<int:dataset_id>' % api_version, methods=['GET'])
def get_dataset(dataset_id):
    return jsonify(mock.dataset)

@app.route('/%s/preview' % api_version, methods=['GET'])
def get_preview():
    return jsonify(mock.preview)

@app.route('/%s/requests' % api_version, methods=['GET'])
def get_requests_list():
    return jsonify(mock.current_requests)

@app.route('/%s/requests' % api_version, methods=['POST'])
def post_request():
    return jsonify(mock.submit_request)

@app.route('/%s/requests/<int:request_id>' % api_version, methods=['GET'])
def get_request(request_id):
    request = (mock.request.copy())["jobId"] = request_id
    return jsonify(request)

@app.route('/%s/requests/<int:request_id>' % api_version, methods=['DELETE'])
def cancel_request(request_id):
    request = (mock.request.copy())["jobId"] = request_id
    return jsonify(request)

if __name__ == '__main__':
    app.run(debug=True)