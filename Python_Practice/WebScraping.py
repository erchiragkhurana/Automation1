import requests
import bs4

#Sending requests with URL
URL = "http://thetestingworld.com"
response = requests.get(URL)

print(response.text) #We will get html of that page
print(response.status_code)

f = open('E:\\result.txt', 'wb') #wb means write binary mode

for data in response.iter_content (10000): #10k bytes
    f.write(data)

f.close()

#Use beautiful soap to parse HTML & XML module, fetch data using CSS locators
URL = "http://thetestingworld.com"
response = requests.get(URL)

parsed_data = bs4.BeautifulSoup(response.text)

all_links = parsed_data.select('a') # a is anchor tag and it will return list of all links
print(len(all_links))

for l in all_links:
    #print(l.gettext())
    print(l.get('href'))
    print(l.get('title'))
    print(l.attrs)