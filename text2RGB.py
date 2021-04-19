usrInput = input('Text to convert to RGB value:')

#Split a string into a given number of substrings
def SplitString(string, divisions):
    return [string[i:i+divisions] for i in range(0, len(string), divisions)]

#Assign a numerical value from 0 to 255 for a given string
def AssignNumericValue(string):
    out = 0
    #Swap case to amplify capital letters
    string = string.swapcase()
    #Get offset for all characters using A as a 1
    A = ord('A')
    for char in string:
        if 'A' <= char <= 'z':
            out += ord(char) - A + 1
    #Set cap of 255
    if out > 255:
        out = 255
    return out

#Output an RGB value given the text input
def ToRGB(text):
    #Stip spaces for processing
    text = text.replace(' ','')

    if len(text) >= 3 and text.isalpha():
        #Concat white space until number divisible by 3
        while (len(text) % 3) != 0:
            text += ' '

        #Split text into R, G, and B
        textRed, textGreen, textBlue = SplitString(text, int(len(text)/3))
        #Remove white space that was added to make string length divisible by 3
        textBlue = textBlue.rstrip()

        print('rgb(' + str(AssignNumericValue(textRed)) + ', ' + str(AssignNumericValue(textGreen)) + ', ' + str(AssignNumericValue(textBlue)) + ')')
    else :
        print('Please enter text longer than 2 characters without numbers or symbols')

ToRGB(usrInput)