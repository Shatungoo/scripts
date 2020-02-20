import requests
import json

config = json.load(open('config.json'))

def service_list():
    data = json.load(open('api_name.json'))
    response = requests.get('http://bb-dev-es-external-6886a9c9fd637f9d.elb.eu-west-1.amazonaws.com:9200/_search',
        json=data,
        auth=(config['username'], config['password'])).json()
    for path in response['aggregations']['2']['buckets']:
        print ('\'' + path['key'] + '\',')
    print ()
service_list()
