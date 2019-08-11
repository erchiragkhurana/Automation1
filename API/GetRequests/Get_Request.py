import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"

response = requests.get(url)
print(response) #it will give the status code only but we want the content
print(response.text) #it will give the result in with full json format (body)
print(response.content) #it will also give the same json format (body)
print(response.headers) #it will give you the headers of the response
print(response.status_code) #it will only give the status code
print(response.cookies)
print(response.encoding)
print(response.elapsed) #time duration of the complete prcoess sending requests and get response
assert response.status_code==200
print(response.headers.get('Date'))
print(response.headers.get('Server'))
print(response.headers.keys())

json_response = json.loads(response.text) #to parse the respknse into json format using json.loads
print(json_response)
pages = jsonpath.jsonpath(json_response,'total_pages')
print(pages[0]) #in this case it has only one value but it returns the list always remeber
assert pages[0]==4

first_name=jsonpath.jsonpath(json_response,'data[0:2].first_name')
print(first_name[1])

first_name=jsonpath.jsonpath(json_response,'data[2].first_name')
print(first_name[0])

for i in range(0,3):
    first_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
    print(first_name[0])
