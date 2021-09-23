#Simple conversion app that I can use to the repo through Git
#Created by John Lovelace

def convertFromCel():
    #Ask for the temperature that the user wants to convert assoc with temp variable
    temp = float(input('What is the temperature that you want to convert? '))
    #Convert and assoc with ftemp variable
    ftemp = (temp * 1.8) + 32
    #Print formated temp
    print("{:.2f}".format(ftemp))


def convertFromFar():
    #Ask for the temperature that the user wants to convert assoc with temp variable
    temp = float(input('What is the temperature that you want to convert? '))
    # Convert and assoc with ftemp variable
    ctemp = (temp - 32) / 1.8
    # Print formated temp
    print("{:.2f}".format(ctemp))

#Ask the user the type of temperature they want to convert assoc with flag variable
flag = input('If you want to convert a Celsius temp enter "C". If you want to convert a Fahrenheit temp enter "F" ')

#While loop to check if the letter entered was correct and to prompt user for proper letter if not
while flag.upper() not in ["C", "F"]:
    flag = input('Please enter a correct letter! ')

#If statement to run the functions determined by the user input
if flag.upper() == "C":
    convertFromCel()
elif flag.upper() == "F":
    convertFromFar()
