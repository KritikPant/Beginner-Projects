#Fibonacci Calculator

import sys
import math

def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x

def isFibonacci(n):
 
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

while True:
    i = input("""
What would you like to do?

1) See the list of Fibonacci numbers
2) See the Nth Fibonacci number
3) See Fibonacci numbers one by one
4) Exit

>>>> """)

    a = 1
    b = 1

    ls = []

    ls.append(a)
    ls.append(b)

    if i == "1":
        print(ls)

        while True:
#             x = input("Press enter to see the next Fibonacci number or press X to return to the main menu: ")
#             if x == "x" or x == "X":
#                 break
            try:
                c = a + b
            except MemoryError:
                print("The number is too large and the computer doesn't have sufficient memory to calculate this...")
                break
                sys.exit
            a = b
            b = c
            ls.append(c)
            if isFibonacci(ls[-1]) == True:
                print(ls)
            else:
                print("ERROR -- Not enough memory")
                break
                sys.exit

    elif i == "2":
        try:
            n = int(input("Input the N value of the Fibonacci number: "))
            if n == 0:
                print("Please input a valid figure above 0")
            elif n == 1:
                print("1")
                break
                sys.exit

            while (n - 2) != 0:
                try:
                    c = a + b
                except MemoryError:
                    print("The number is too large and the computer doesn't have sufficient memory to calculate this...")
                    break
                    sys.exit
                a = b
                b = c
                ls.append(c)
                n = n - 1

            if (n - 2) == 0:
                if isFibonacci(ls[-1]) == True:
                    print(ls[-1])
                    sys.exit
                else:
                    print("ERROR -- Not enough memory")
                    break
                    sys.exit
        except ValueError:
            print("Please enter a number... ")        

    elif i == "3":
        print(a)
        print(b)
        while True:
            x = input("Press enter to see the next Fibonacci number or press X to return to the main menu: ")
            if x == "x" or x == "X":
                break
            try:
                c = a + b
            except MemoryError:
                print("The number is too large and the computer doesn't have sufficient memory to calculate this...")
                break
                sys.exit
            a = b
            b = c
            ls.append(c)
            if isFibonacci(ls[-1]) == True:
                print(ls[-1])
            else:
                print("ERROR -- Not enough memory")
                break
                sys.exit

    elif i == "4":
        sys.exit()

    else:
        print("Please enter a valid choice...")
        
    
          
