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


def solution(celsius):
    celsius = float()
    fahrenhei = (celsius * 9 / 5) + 32
    fahrenheit = round(fahrenhei, 2)
    return fahrenheit


def solution(meters):
    meters = float(meters)
    centimeters = 100 *meters
    mililmeters = 1000*meters
    return f"Centimeters: {centimeters}.\nMillimeters: {millimeters}."


def solution(kilograms):
    kilograms = float(kilograms)
    grams = 1000 * kilograms
    pounds = round(kilograms * 2.20462, 2)

    return f"Kilograms: {kilograms}\nGrams: {grams}\nPounds: {pounds}"


grace = "Omale"
if grace == "Omale":
    grace = "Omale Grace"
    print(grace)


def solution(value):
    try:
        value = float(value)
        value = round(value * 2, 2)
        return value
    except ValueError:
        return "Invalid number"


