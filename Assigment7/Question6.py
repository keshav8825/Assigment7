"""Write a python program to check whether a given string is a multiword string or single
   word string using match case statement"""
a=input("Enter a string: ")
match a:
    case a if ' ' in a:
        print("Multiword String")
    case b if ' ' not in a:
        print("Single line string")
        
