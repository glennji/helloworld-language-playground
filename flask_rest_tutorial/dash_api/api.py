from flask import Flask, request, jsonify
from flask.ext.restful import Api, Resource
import mock_responses as mock

api_version = "v1"

app = Flask(__name__)
api = Api(app)


class CollectionList(Resource):
    def get(self):
        return jsonify(mock.collections)


class Collection(Resource):
    def get(self, collection_id):
        c = mock.collection.copy()
        c["id"] = collection_id
        return jsonify(c)


class CollectionDatasetList(Resource):
    def get(self, collection_id):
        return jsonify(mock.collection_dataset)


class DatasetList(Resource):
    def get(self):
        return jsonify(mock.datasets)


class Dataset(Resource):
    def get(self, dataset_id):
        return jsonify(mock.dataset)


class Preview(Resource):
    def get(self):
        return jsonify(mock.preview)


class RequestList(Resource):
    def get(self):
        return jsonify(mock.current_requests)

    def post(self):
        q = request.json["query"]
        r = mock.submit_request.copy()
        r["request"]["query"] = q
        return jsonify(r)


class Request(Resource):
    def get(self, request_id):
        r = mock.request.copy()
        r["jobId"] = request_id
        return jsonify(r)

    def delete(self, request_id):
        r = mock.cancel_request.copy()
        r["jobId"] = request_id
        return jsonify(r)

api.add_resource(CollectionList, '/%s/collections' % api_version)
api.add_resource(Collection, '/%s/collections/<string:collection_id>' % api_version)
api.add_resource(CollectionDatasetList, '/%s/collections/<string:collection_id>/datasets' % api_version)

api.add_resource(Preview, '/%s/preview' % api_version)

api.add_resource(DatasetList, '/%s/datasets' % api_version)
api.add_resource(Dataset, '/%s/datasets/<string:dataset_id>' % api_version)

api.add_resource(RequestList, '/%s/requests' % api_version)
api.add_resource(Request, '/%s/requests/<int:request_id>' % api_version)

if __name__ == '__main__':
    app.run(debug=True)
