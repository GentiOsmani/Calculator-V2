import re

print("calculator v2")
print("type 'quit' to exit the calculator")

previous = 0
run = True

def performMath():

    global run
    global previous
    equation = ''
    if previous == 0:
        equation = input("enter equation here: ")
    else:
        equation = input(str(previous))
    
    if equation == "quit":
        print("Thanks for using Calculator V2!")
        run = False
    
    else:
        equation = re.sub('[a-zA-z:;]', ' ', equation)

    if previous == 0:
        previous = eval(equation)
    else:
        previous = eval(str(previous)+ equation)

while run:
    performMath()
