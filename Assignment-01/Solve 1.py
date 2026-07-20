# Mr. Rahman is grading a quiz, but he has a rule: he always drops the single highest score before
# calculating the class average, so one lucky genius doesn't skew the curve.
# Given a list of scores, write code that:
# 1. Finds the maximum score in the list.
# 2. Removes one occurrence of that maximum score.
# 3. Calculates and prints the average of the remaining scores.
# scores = [78, 92, 85, 92, 60, 74]
# # Expected: remove one 92, then average the rest



def fairgrade(scores):
    max = scores[0]
    idx=0
    for i in range(len(scores)):
        if(scores[i]>max):
            max=scores[i]
            idx=i
    scores.pop(idx)
    sum=0
    for val in scores:
        sum+=val
    avg = sum/len(scores)
    print(f'Average : {avg}')

marks = [78, 92, 85, 92, 60, 74]
fairgrade(marks)