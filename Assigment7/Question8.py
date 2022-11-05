""" Write a python script to check whether two given strings are identical, first string
   comes before the second in dictionary order or first string comes after the second
   string in dictionary order using match case statement"""
a=input("Enter first string ")
b=input("Enter second string ")
match(a,b):
    case (a,b) if a==b:
        print("Identical string")
    case (a,b) if a>b:
        print("{} comes after {}".format(a,b))
    case (a,b) if a<b:
        print("{} comes after {}".format(b,a))
        
              
