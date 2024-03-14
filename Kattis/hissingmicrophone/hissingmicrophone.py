'''
Name: Janet Griffin
Date: 3/13/2024
Program:Kattis Hissing Microphone https://open.kattis.com/problems/hissingmicrophone
Algorithm Steps: 
    Program will check to see if input string has two or more consecutive 's'es:
    if yes, print "hiss"
    if no, print "no hiss"
'''
word = str(input())

if 'ss' in word:
    print("hiss")
else:
    print("no hiss")

    