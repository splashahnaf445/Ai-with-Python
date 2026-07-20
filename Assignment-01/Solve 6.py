# Problem 6: The Fair Average (Lists, revisited)
# A judge is scoring a talent show with 5 judges. To avoid bias, the show organizers drop both the
# highest and the lowest score before averaging the rest.
# Given a list of 5 scores, write code that:
# 1. Removes one occurrence of the maximum score.
# 2. Removes one occurrence of the minimum score.
# 3. Prints the average of the remaining 3 scores.
# judge_scores = [8, 9, 7, 10, 6]

def fairjudge(scores):
    maximum=scores[0]
    idx=0
    for i in range(len(scores)):
        if(scores[i]>maximum):
            maximum=scores[i]
            idx=i
    scores.pop(idx)
    min=scores[0]
    idx=0
    for i in range(len(scores)):
        if(scores[i]<min):
            min=scores[i]
            idx=i
    scores.pop(idx)
    sum=0
    for val in scores:
        sum+=val
    avg=sum/len(scores)
    return avg

judge_scores = [8, 9, 7, 10, 6]
x=fairjudge(judge_scores)
print(f'Average : {x}')

