#!/usr/bin/python3

#This program illustrates a choatic function
def main():
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter a second number between 0 and 1: "))
    n=eval(input("How many numbers should I print? ") )
    for i in range(n):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)

        print(x, y)

main()
