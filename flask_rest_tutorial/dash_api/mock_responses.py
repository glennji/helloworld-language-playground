
collections = {
    "meta": {
        "nextResults": {
            "href": "/collections?offset=9&limit=3",
            "type": "application/json",
            "method": "GET",
            "rel": "next",
            "title": "Next results"
        },
        "previousResults": {
            "href": "/collections?offset=3&limit=3",
            "type": "application/json",
            "method": "GET",
            "rel": "prev",
            "title": "Previous results"
        }
    },
    "collections": [{
                        "name": "Awesome collection",
                        "id": "sirca.cg",
                        "description": "This is an awesome collection",
                        "longDescription": "This is an awesome collection "
                    }]
}

collection = {
    "name": "Awesome collection",
    "id": "sirca.cg",
    "description": "This is an awesome collection",
    "longDescription": "This is an awesome collection "
}

collection_dataset = {
    "datasets" : [{
                      "name": "Awesome collection",
                      "id": "cg.directors",
                      "collections": ["sirca.cg"],
                      "description": "This is an awesome collection",
                      "longDescription": "This is an awesome collection, spanning ",
                      "categories": ["category1", "category2", "category3"],
                      "keywords": ["keyword1", "keyword2"],
                      "source": "Australian Stock Exchange",
                      "fields": [{
                                     "id": "field1",
                                     "title": "Field 1",
                                     "type": "string",
                                     "description": "Field 1 is the first field of the data set"
                                 },{
                                     "id": "field2",
                                     "title": "Field 2",
                                     "type": "number",
                                     "description": "Field 2 is the second field of the data set"
                                 },{
                                     "id": "field3",
                                     "title": "Field 3",
                                     "type": "date",
                                     "description": "Field 3 is the second field of the data set"
                                 }]
                  }]
}

datasets =  {
    "meta": {
        "nextResults": {
            "href": "/datasets?query=director&offset=9&limit=3",
            "type": "application/json",
            "method": "GET",
            "rel": "next",
            "title": "Next results"
        },
        "previousResults": {
            "href": "/datasets?query=director&offset=3&limit=3",
            "type": "application/json",
            "method": "GET",
            "rel": "prev",
            "title": "Previous results"
        }
    },
    "datasets": [{
                     "name": "Awesome dataset",
                     "id": "cg.directors",
                     "collections": ["sirca.cg"],
                     "description": "This is an awesome dataset",
                     "longDescription": "This is an awesome dataset, spanning ",
                     "categories": ["category1", "category2", "category3"],
                     "keywords": ["keyword1", "keyword2"]
                 }]
}

dataset = {
    "name": "Awesome dataset",
    "id": "cg.directors",
    "collections": ["sirca.cg"],
    "description": "This is an awesome dataset",
    "longDescription": "This is an awesome dataset, spanning ",
    "categories": ["category1", "category2", "category3"],
    "keywords": ["keyword1", "keyword2"],
    "source": "Australian Stock Exchange",
    "fields": [{
                   "id": "field1",
                   "title": "Field 1",
                   "type": "string",
                   "description": "Field 1 is the first field of the data set"
               },{
                   "id": "field2",
                   "title": "Field 2",
                   "type": "number",
                   "description": "Field 2 is the second field of the data set"
               },{
                   "id": "field3",
                   "title": "Field 3",
                   "type": "date",
                   "description": "Field 3 is the second field of the data set"
               }]
}

preview = {
    "data":
        [{
             "field1": "[row1;field1]",
             "field2": 1.2
         },{
             "field1": "[row2;field1]",
             "field2": 2.2
         },{
             "field1": "[row3;field1]",
             "field2": 3.2
         }],

    "meta": {
        "nextResults": {
            "href": "/data?query=select * from cg.directors&offset=9&limit=3",
            "type": "application/json",
            "method": "GET",
            "rel": "next",
            "title": "Next results"
        },
        "previousResults": {
            "href": "/data?query=select * from cg.directors&offset=3&limit=3",
            "type": "application/json",
            "method": "GET",
            "rel": "prev",
            "title": "Previous results"
        }
    }
}

submit_request = {
    "jobId": "34234",
    "status": "pending",
    "request" : {
        "query": "select * from table_name",
        "format": "csv",
        "destination": {
            "type":"s3",
            "location": "s3://my.bucket/path/to/file.csv"
        },
        "completionAction" : {
            "type":"http_post",
            "url":"http://my.server/path/to/callback"
        }
    }
}

current_requests = {
    "requests": [
        {
            "jobId": "34234",
            "status": "pending"
        },
        {
            "jobId": "34235",
            "status": "running"
        },
        {
            "jobId": "34236",
            "status": "running"
        }
    ],
    "meta": {
        "nextResults": {
            "href": "/requests?offset=9&limit=3",
            "type": "application/json",
            "method": "GET",
            "rel": "next",
            "title": "Next results"
        },
        "previousResults": {
            "href": "/requests?offset=3&limit=3",
            "type": "application/json",
            "method": "GET",
            "rel": "prev",
            "title": "Previous results"
        }
    }
}

request = {
    "jobId": "34234",
    "status": "complete",
    "request" : {
        "query": "select * from table_name",
        "format": "csv",
        "destination": {
            "type":"s3",
            "location": "s3://my.bucket/path/to/file.csv"
        },
        "completionAction" : {
            "type":"http_post",
            "url":"http://my.server/path/to/callback"
        }
    }
}

cancel_request = {
    "jobId": "34234",
    "status": "canceled",
    "request": {
        "query": "select * from table_name",
        "format": "csv",
        "destination": {
            "type": "s3",
            "location": "s3://my.bucket/path/to/file.csv"
        },
        "completionAction": {
            "type": "http_post",
            "url": "http://my.server/path/to/callback"
        }
    }
}