#!/usr/bin/python 

# This is reverse Cipher 
# Author savio 
# Chapter 4 of CCWP

message = "This is string to be reversed, This is " + \
           "encryption we don't want"

def reverseString(string):
    lengthOfString = len(string) - 1
    tempString = ""
    while lengthOfString >= 0:
        tempString = tempString + string[lengthOfString]
        lengthOfString -= 1 

    return tempString

if __name__ == '__main__':
    
    print("[+] The reverse string is ")
    print("\n-------------------------\n")
    print(reverseString(message))
    print("[+] The reverse string is ")
    print("\n-------------------------\n")
    print(reverseString(reverseString(message)))

