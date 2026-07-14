#INput

print("Enter a number: ")

a= int(input())

print("You entered:", a)

a=input()

print(f"You entered : {a}")
print(type(a))

b=input('Enter your name: ')
print(f"Your name is: {b}")


#loop

#loop iterate while skipping numbers
for i in range(0,10,3):
    print(i)


#List

arr=['apple', 'banana', 'cherry']
print(arr)

#problem 1

## print all pair of numbers from a list

l = [1, 2, 3, 4, 5]

for i in range(len(l)):
    for j in range(i+1,len(l)):
        print(l[i],l[j])


## write a code that counts the frequency of a letter in a sentence

sentence = "The fox ran over the lazy dog"
x=sentence.count("e")
print(f'Frequency of e is : {x}')



## write a code that counts the frequency of all letters in a sentence
# Use dictionary type : {}
# Dictionary : 'name' : 'ahnaf' ......

## write a code that counts the frequency of each letter in a sentence

sentence = "I live in Bangladesh"

freq = {}
print(type(freq))

for i in range(len(sentence)):
    char = sentence[i].lower()
    if char not in freq:
        freq[char]=0
    freq[char]=freq[char]+1

for char in freq:
    print(f"{char}:{freq[char]}")

print(freq)


