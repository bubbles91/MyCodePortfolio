cardNo = input("Please enter the card number you would like to verify? ")

def LuhnCheck(cardNo):
    s = []
    amex = 'AmEx'
    master = 'Mastercard'
    visa = 'Visa'
    manu = ''
    manuNum = 0

    isSecond = False
    nDigits = len(cardNo)
    nSum = 0

    for i in range(0,2):
        s.append(cardNo[i])
    manuNum = int((s[0]) + (s[1]))

    if manuNum == 35 or manuNum == 37:
        manu = amex
    elif manuNum > 50 and manuNum < 56:
        manu = master
    elif int(s[0]) == 4:
        manu = visa

    for i in range(nDigits -1, -1, -1):
        d = ord(cardNo[i]) - ord('0')
        if isSecond:
            d = d * 2
            nSum += d // 10
            nSum += d % 10
            isSecond = False

    if nSum % 10 == 0:
        print(manu)
        print('Valid')
    else:
        print('Invalid')