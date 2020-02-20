import requests
import json

services = ['products']
data = json.load(open('request.json'))
config = json.load(open('config1.json'))

for service_name in services:
    print (service_name)
    data['query']['bool']['must'][2]['match_phrase']['api.keyword']['query'] = service_name
    response = requests.get(config['url'],
        json=data,
        auth=(config['username'], config['password'])).json()
    with open(service_name,'w') as file:
        print(json.dumps(response, indent=2))
        for path in response['aggregations']['2']['buckets']:
            file.writelines(path['key']+ '\n') 
