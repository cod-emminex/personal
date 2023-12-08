#!/usr/bin/python3

# convert.py
# a program that converts temperature figures from celsius to fahrenheit
# cod-emminex

def main():
    celsius = eval(input("Enter your temperature in Celsius: "))
    fah = 9/5 * celsius + 32
    print(f"The temperature in Fahrenheit is {fah} degree Fahrenheit")

main()
