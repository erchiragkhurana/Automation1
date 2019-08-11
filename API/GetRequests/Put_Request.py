import requests
import json
import jsonpath

url = "https://reqres.in/api/users/2" #with id

file = open('..\\..\\API\\json_PUT.json','r').read()  #First open the file and read its content (file handling)
print(file)
json_file=json.loads(file) #now convert it  itno json formt which we are going to send via PUT

response = requests.put(url,json_file) #we need to pass body in form of json file
print(response.content)
assert response.status_code==200
print(response.headers)
print(response.headers.get('Content-Length'))

#Now whn we have put something and if we want to get the data again ij json format from string format then we have to parse it
jsonr_afterPut =json.loads(response.text) #always make sure to chnage it into text or content
print(jsonr_afterPut)

#now of you want to pick something from json then we need to use jsonpath
updated_time = jsonpath.jsonpath(jsonr_afterPut,'updatedAt') #always make sure this will going to return a list or you can say dictionary too
print(updated_time[0])
