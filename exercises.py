#Temporary programming file for exercises in The Coder's Apprentice

'''import math

a = input("Please enter the first number: ")
a_num = int(a)
b = input("Please enter the second number: ")
b_num = int(b)
c = input("Please enter the third number: ")
c_num = int(c)

print("Max of three numbers is : ", max(a_num, b_num, c_num))
print("Min of three numbers is : ", min(a_num, b_num, c_num))
print("Average of three numbers is : {}".format((a_num+b_num+c_num)/3))
'''


'''
import sys

num = input("Please enter a positive integer: ")
if int(num) < 0:
    print("You should have entered a positive integer")
    sys.exit()
else:
    print("Now I am processing your integer", num)
    print("Lots and lots of processing")
    print("Hunders of lines of code here")
'''

#Exercise 6.1
'''
from sys import exit

grade = input("Please enter the numeric grade: ")
grade = float(grade)
if grade<0 or grade>10:
    print("Please enter a numeric grade in [0,10].")
elif 2*float(grade)%1 != 0:
    print("Grade must be in increments of 0.5.")
    exit()
elif grade >= 8.5:
    print("Grade is A.")
elif grade >=7.5:
    print("Grade is B.")
elif grade >=6.5:
    print("Grade is C.")
elif grade >=5.5:
    print("Grade is D.")
else:
    print("Grade is F.")

print("Done with grade translation! Bye!!")
'''

#Exercise 6.3
'''
UserString = input("Enter a string: ")
VowelCount = 0
if "a" in UserString:
    VowelCount = VowelCount + 1
if "e" in UserString:
    VowelCount = VowelCount + 1
if "i" in UserString:
    VowelCount = VowelCount + 1
if "o" in UserString:
    VowelCount = VowelCount + 1
if "u" in UserString:
    VowelCount = VowelCount + 1

print("There are", VowelCount, "different vowels in the string")
'''

#TODO Exercise 6.4

#Exercise 8.1
'''
def printMulTable(num):
    for i in range(1, 11):
        print(i*num)
    return

num = input("Provide a number: ")
printMulTable(int(num))
'''

#Exercise 8.2
'''
def removeDuplicates(string):
    tempStr = ""
    for i in range(0, len(string)):
        if string[i] in string[i+1:len(string)]:
            continue;
        else:
            tempStr += string[i]
    return tempStr
        

def numOfCommonChars(string1, string2):
    count = 0
    string1 = removeDuplicates(string1)
    for i in range(0, len(string1)):
        if string1[i] in string2:
            count += 1
        else:
            continue
    return count

count = numOfCommonChars("beep", "peer")
print("Number of common characters: ", count)
'''

#Exercise 8.3
'''
#Note: Converges very very slowly
def piApprox(numOfTerms):
    temp = 0
    sign = +1
    for i in range(1, numOfTerms*2-1, 2):
        temp += sign*(1/i)
        #print(sign)
        #print(temp)
        sign *= -1
    piApprox = 4 * temp
    return piApprox

print(piApprox(300))
'''
        
#Exercises 8.4, 8.5, 8.6

#Exercises 10.1, 10.2, 10.4, 10.5, 10.6

print("Hello World")
print("trying out github")
print("yadaya - only commit no push")





    







































