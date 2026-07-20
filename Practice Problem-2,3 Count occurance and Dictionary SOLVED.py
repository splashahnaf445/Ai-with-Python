# Problem 2 - Word Frequency Counter
# Write a function word_frequency(text) that takes a string of text and returns a dictionary
# mapping each word to how many times it appears

# Requirements:
# ● Return the dictionary sorted by frequency, highest first (you can return a list of tuples for
# this, or a regular dict).
# Then write a function most_common_word(text) that reuses word_frequency to return the
# single most frequent word



def word_frequency(text):
    freq={}
    word = []
    text=text.lower()
    word=text.split()
    for w in word:
        if w in freq:
            freq[w]+=1
        else:
            freq[w]=1
    return sorted(
        freq.items(),
        key = lambda item : item[1],  #lambda chooses the item to sort, item[1] means value (Here frequency of the word) (0:key, 1:value)
        reverse=True  # highest first meanse descending

    )

string = input('Give a sentence : ')

# for w in freq:
#     print(f'{w} : {freq[w]}')

print((word_frequency(string)))

# return dictionary sorted by frequency


def most_common_word(text):
    sorted_words = word_frequency(text)
    print(sorted_words[0][0])

print(most_common_word(string))



# Problem 3: Grade Book
# Description
# You're tracking grades for a class of students. You're given a dictionary where keys are student
# names and values are lists of their test scores:
# grades = { "Alice": [90, 85, 92],
# "Bob": [70, 65, 80],
# "Charlie": [88, 91, 95],
# } W
# rite these functions:
# ● average(scores): takes a list of numbers, returns the average (float).
# ● student_average(grades, name): returns the average score for one student.
# Print a report showing each student's average and letter grade, then print the top student and
# the overall class average.

grades = { "Alice": [90, 85, 92],
 "Bob": [70, 65, 80],
 "Charlie": [88, 91, 95],
}


def average(scores):
    sum=0
    count=0
    for i in scores:
        sum+=i
        count+=1
    avg = sum/count

    return avg

x=average([15,45,96,41])
print(x)

def student_average(grades, name):
    for i in grades:
        if i.lower()==name.lower():
            mark=average(grades[i])
            return mark



str1 = input('give student name : ')
avg=student_average(grades,str1)
print(avg)

#report
def letter_grade(avg):
    if(avg>=90):
        return 'A'
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"
    

    
for student in grades:
    g=student_average(grades,student)
    Letter=letter_grade(g)
    print(f'{student} : Average : {g}, Letter grade : {Letter}')





