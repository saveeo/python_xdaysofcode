#!/usr/bin/python

'''
This program reverse the string with help of pythonic notion
Author : savio

'''

message = "This is the string we want to reverse, not good example but any" + \
          "ways this is what we get"

def reverseString(message):
  string = [message[ch] for ch in range(-1, -(len(message)+1), -1)]
  return "".join(string)


if __name__ == '__main__':
  print("[+] reverse string of {}".format(message))
  print("\n" + "-"*10 + "\n")
  print(reverseString(message))
  
  print(reverseString(reverseString(message)))
