# Problem 3: The Attendance Counter (Functions)
# Every morning, a teacher calls out student names, and marks who is present in a list. Write a
# function called count_present that takes a list of names (with possible repeated names if someone
# got marked twice by mistake) and returns how many unique students were present.
# def count_present(names):
# # your code here
# pass
# attendance = ["Amina", "Karim", "Amina", "Nabil", "Karim", "Sara"]
# print(count_present(attendance)) # should print 4

def count_present(names):
    lists=[]
    for name in names:
        if(name not in lists):
            lists.append(name)
    count=0
    for i in range(len(lists)):
        count+=1
    return count

attendance = ["Amina", "Karim", "Amina", "Nabil", "Karim", "Sara"]
print(count_present(attendance))