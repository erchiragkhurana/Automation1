import requests
import json
import jsonpath

url = "https://reqres.in/api/users" #without id

file = open('..\\..\\API\\json_POST.json','r').read()  #First open the file and read its content (file handling)
print(file)
json_file=json.loads(file) #now convert it  itno json formt which we are going to send via POST

response = requests.post(url,json_file) #we need to pass body in form of json file
print(response.content)
assert response.status_code==201
print(response.headers)
print(response.headers.get('Content-Length'))

#Now whn we have post something and if we want to get the data again ij json format from string format then we have to parse it
jsonr_afterPost =json.loads(response.text) #always make sure to chnage it into text or content
print(jsonr_afterPost)

#now of you want to pick something from json then we need to use jsonpath
id = jsonpath.jsonpath(jsonr_afterPost,'id') #always make sure this will going to return a list or you can say dictionary too
print(id[0])
