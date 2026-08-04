def solution(name):
    return f"Hello, {name}. Welcome to Talent Nation."
print(solution)


def solution(name,track):
    return f"{name} is starting the {track}."


def solution(name, cohort):
    return f"Name: {name}\nCohort: {cohort}\nStatus: Ready"


def solution(name, a, b, c):
    sum = a + b + c
    averag = sum/3
    average = round(averag, 2) #this rounds the number to 2 decimal place
    maximum = max(a,b,c) #this gets the maximum number
    return f"Student: {name}\nSum: {sum}\nAverage: {average}\nMaximum: {maximum}"