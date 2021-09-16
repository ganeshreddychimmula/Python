#tuple=1,  #this is a tuple
#tuple=(1,) #this data is of type tuple
#tuple=(1) #this datya is of type 'int'
dict = {"cat" : "chat", "zoat" : "chien", "horse" : 3.0}
phoneNumbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
emptyDictionary = {}
#dict=sorted(dict.keys())
y=dict.items()
print(y)
print(type(phoneNumbers))
print(emptyDictionary)
dict["cat"]="brat"
dict["us"]="shit"
dict.update({"royal enfield":"love"})
print(dict)
del dict['royal enfield']
print(dict)
dict.popitem()#removes last item
print(dict)
