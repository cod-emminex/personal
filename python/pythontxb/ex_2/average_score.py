#!/usr/bin/python3

# a program to print the average of numbers

def main():
    text = "This program calculates the average of scores"
    print(f"{text:=^70}")
    score1, score2 = eval(input("Please input two scores separated by comma: "))
    score = (score1 + score2) / 2
    print("The average score is", score)

main()
