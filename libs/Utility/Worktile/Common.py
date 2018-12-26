# -*- encoding:UTF-8 -*-
import requests
import json

headers = {
    'Content-type': 'application/json',
    "authorization": "Bearer 6HQJokkpfMcmxjtKSyqvFz1aYdrTYr9h4zE5RUfEWS3j904ZzYMb0SIacuH2nmCTC5Oxi4uFMcmGa2XKU7mSsbmETdy2rvIDZ79dogaDwJmSAGYW89cAIbKg4RZwj9lcdN3Tw39Cusr90MEHO9TPcAm8jkIv3vkF5qPHdG9qWZ5w2IzXJVNrzY1yhyYvE4AaY2702mQ6Qc65ce5Jq1QxLyQEuYD8bjEoKDBWVtaewmJ8WcX0vKiBXVYWvsv6VH8f"
}


def JSON_DUMPS(data):
    return json.dumps(data)


def JSON_LOADS(data):
    return json.loads(data)


def POST(url, data):
    session = requests.Session()
    session.headers = headers
    resp = session.post(url=url, data=data)
    return resp


def GET(url):
    session = requests.Session()
    session.headers = headers
    resp = session.get(url=url)
    return resp
