# Write your code here

# TASK 1

def hello():
    return "Hello!"

# TASK 2

def greet(name):
    return f"Hello, {name}!"

# TASK 3

def calc(a, b, operation="multiply"):
    try:
        if operation == "add":
            return a+b
        elif operation == "subtract":
            return a-b
        elif operation == "multiply":
            return a*b
        elif operation == "divide":
            return a/b
        elif operation == "modulo":
            return a%b
        elif operation == "int_divide":
            return a//b
        elif operation == "power":
            return a**b
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"


# TASK 4

def data_type_conversion(value, type):
    try:
        if type == "float":
            return float(value)
        elif type == "str":
            return str(value)
        elif type == "int":
            return int(value)
    except ValueError:
        return f"You can't convert {value} into a {type}."

# TASK 5

def grade(*args):
    try:
        average = sum(args)/len(args)

        if average >= 90:
            return "A"
        elif average >=80:
            return "B"
        elif average >=70:
            return "C"
        elif average >=60:
            return "D"
        else:
            return "F"
    except:
        return "Invalid data was provided."

# TASK 6

def repeat(string, count):
    newString = ""
    for i in range(count):
        newString += string

    return newString

# TASK 7

def student_scores(option, **kwargs):
    if option == "best":
        best_student = ""
        best_score = 0

        for name, score in kwargs.items():
            if score > best_score:
                best_score = score
                best_student = name

        return best_student

    elif option == "mean":
        return sum(kwargs.values()) / len(kwargs.values())

# TASK 8

def titleize(title):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = title.split()
    result = []

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word not in little_words:
            result.append(word.capitalize())
        else:
            result.append(word)

    return " ".join(result)

# TASK 9

def hangman(secret, guess):
    result = ""

    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result +="_"

    return result

# TASK 10

def pig_latin(string):
    words = string.split()
    vowels = ["a", "e", "i", "o", "u"]
    result = []

    for word in words:
        if word[0] in vowels:
            result.append(word + "ay")
        else:
            for i, letter in enumerate(word):
                if letter in vowels:
                    if word[i-1:i+1] == "qu":
                        i += 1
                    result.append(word[i:] + word[:i] + "ay")
                    break
    return " ".join(result)