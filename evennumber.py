#!/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
#n = input("enter the value for n")

if (n%2 == 0) and n in range(1,100) and n in range(2,5):
    print('Not Weird')
elif (n%2 == 0) and n in range(1,100) and n in range(5,21):    
    print('Weird')
elif (n%2 == 0) and n in range(1,101) and n >20:    
    print('Not Weird')    
elif (n%2 == 1) and n in range(1, 100):
    print('Weird')   
else:
    print('enter valid value')    