import requests
import json
import jsonpath


dics ='{"k1":"khurana","k2":"khurana147"}'
json_result = json.loads(dics)

print(json_result['k1'])

#Send request to api, then parse the response to json, then validate it by json path

api_url = "https://reqres.in/api/users?page=2"

# Make a request
response1 = requests.get(api_url)
print(response1.text)

# Validate Status code
assert response1.status_code == 200

# Parse response into JSON format
json_response = json.loads(response1.text)

print(json_response)

# Apply JSON Path
x = jsonpath.jsonpath(json_response, 'total')
print(x[0])
y = jsonpath.jsonpath(json_response, 'data[2].last_name')
print(y[0])

for val in json_response['data']:
    print(val['first_name'])