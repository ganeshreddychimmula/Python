#problem:
# #HackerLand University has the following grading policy:
#Every student receives a grade in the inclusive range from 1 to 100.
#Any 40 less than  is a failing grade.
#Sam is a professor at the university and likes to round each student's grade's according to these rules:

#If the difference between the grade  and the next multiple of 5 is less than 3, round  up to the next multiple of .
#If the value of  is less than 38, no rounding occurs as the result will still be a failing grade.

#input format:Input Format
#The first line contains a single integer n , the number of students.
#Each line  of the  subsequent lines contains a single integer, grades[i]

#sample input:
#4
#73
#67
#38
#33
#DESCRIPTION:given 5n-grade<3 -> grade=5n
#if grade<38 no grade and fail
#if grade<40 no grade fail
#if grade/5>2 -> round to next 5

#solution:

# function to change grades:
def rounding(g):
    final=[]
    if n>=0 and n<=60 :
        for i in range(n):
            if g[i]<38:
               final.append(g[i])
            elif g[i]%5<=2:
                final.append(g[i])
            else:
               final.append(g[i]-(g[i]%5)+5)
    return final


# taking input
n=int(input())
grade=[]
for i in range(n):
    grade.append(int(input().strip()))
#final_grade=rounding(grade)
for i in rounding(grade):
    print(i)