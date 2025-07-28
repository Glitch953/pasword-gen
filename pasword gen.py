#Random Password Generator - www.101computing.net/random-password-generator/
import random
#A function do shuffle all the characters of a string
def shufflee(string):
    templist = list(string)
    random.shuffle(templist)
    return ''.join(templist)

#Main program starts here
uppercaeLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaeLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaeLetter3=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaeLetter4=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaeLetter5=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
#Generate password using all the characters, in random order
password = uppercaeLetter1 + uppercaeLetter2 + uppercaeLetter3 + uppercaeLetter4 + uppercaeLetter5 # + .....
password = shufflee(password)

#output
print(password)
