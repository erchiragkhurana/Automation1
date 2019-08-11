#Values are stored in the form of key value pair
#We use curly brackets for dictionary {}
#Key must always be unique \
#Key and value could be of any data type like list and tuple
#Values can be fetched by passing keys

Dics={"Chirag":148,"Khurana":147,"Chirag":147,"Testing":"Python",4:"None",5:170}
print(Dics)
print(Dics["Chirag"])

#to update or add a value for key, we can also add at the end/between of the dictionary or by the below way
Dics[4] = 5
print(Dics)

#dictionary functions - keys and values operations
print(Dics.keys())
print(Dics.values())

#to find all the items we use item function in normal and big bracket
print(Dics.items())