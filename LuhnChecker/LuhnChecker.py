# Ask for the card number from the user
cardNo = input("Please enter the card number you would like to verify? ")

def LuhnCheck(cardNo):
    # Init variables for card manufacturer
    s = []
    amex = 'AmEx'
    master = 'Mastercard'
    visa = 'Visa'
    manu = ''
    manuNum = 0

    # Init variables for Luhn checker
    isSecond = False
    nDigits = len(cardNo)
    nSum = 0
    
    # Append the first two numbers to a list
    for i in range(0,2):
        s.append(cardNo[i])
    # Concat the numbers and cast to int
    manuNum = int((s[0]) + (s[1]))

    # If statements to find manufacturer
    if manuNum == 35 or manuNum == 37:
        manu = amex
    elif manuNum > 50 and manuNum < 56:
        manu = master
    elif int(s[0]) == 4:
        manu = visa
    else:
        manu = 'Unknown'

    # For statement to check numbers backwards, uses the unicode value to get the number
    for i in range(nDigits -1, -1, -1):
        d = ord(cardNo[i]) - ord('0')
        # Bool value decides if the number is the second from last and continues to cycle throughout the iteration
        if isSecond:
            d = d * 2
            # If number is double digit floor division and modulo separate the digits and add them
            nSum += d // 10
            nSum += d % 10
            isSecond = False

    # If the modulo of the sum is 0 print valid and manufacturer
    if nSum % 10 == 0:
        print(manu)
        print('Valid')
    else:
        print('Invalid')