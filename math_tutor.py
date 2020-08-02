from random import randrange as r
from time import time
score = 0
question = []
qn = int(input("enter the number of questions: "))
max = int(input("enter the maximum range of number: "))
start = time()
for i in range(qn):
    num1 , num2 = r(1,max+1), r(1,max+1)
    og_ans = num1*num2
    my_ans = int(input(f"{num1}*{num2} = "))
    question.append(f"{num1}*{num2} = {og_ans} Your Answer: {my_ans}")
    if my_ans == og_ans:
        score+=1
    end = time()
    t_time = end - start
print(f"Thanks for playing!! you scored:{score} out of {qn} with {round((score/qn)*100)}%\n you took {round(t_time,1)} secs {round((t_time/qn),1)}per question")

for a in question:
    print(a)



