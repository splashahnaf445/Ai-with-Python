import math

list=[1,2,3,'ahnaf','bd',10.59,(1,2,3),9]

print(list)

print(list[4],list[7])

#INSERT only at last    : Use append
list.append('python')

#insert Shahriar after 3rd index : Use insert

list.insert(4,'shahriar')

print(list)

#DELETE using Index    : Use pop
list.pop(2)

#DELETE using value    : Use remove
list.remove('bd')
print(list)

#Printing a list in seperate
for item in list:
    print(item)

#Slicing : Slice and fetch items from a list (1st index : last idx+1 ) to create a new list
#fetch 2nd to 6th item in the list
temp = list[1:6]
print(temp)

#Copy a list : use copy
gpt = [11,57,9,8,346,79]
gemini = gpt.copy()
print(gpt,gemini)

#Dictionary : Pair of key:value ; can search a value using key
myself = {
    'name' : 'ahnaf',
    'age' : 23,
    'location' : 'bd',
    10 : 56,
    18 : 'Birthday'
}

print(myself['name'])
print(myself[18])

## write a code that counts the frequency of each letter in a sentence

sentence = "I study in UIU"

counter = {}
for i in range(len(sentence)):
    char = sentence[i].lower()
    if char not in counter:
        counter[char]=0
    counter[char]=counter[char]+1
    
for char in counter:
    print(f"{char}:{counter[char]}")

print(counter)


#Problem 3 : # calculate the distance between two points

def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

x=distance(1,1,4,5)
print(x)


