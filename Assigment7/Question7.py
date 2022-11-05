"""Write a python program to check whether a given number is positive, negative or
   zero using match case statement"""
a=int(input("Enter a number:"))
match a:
    case a if a>0:
        print("Positive")
    case a if a<0:
        print("negative")
    case a if a==0:
        print("zero")
