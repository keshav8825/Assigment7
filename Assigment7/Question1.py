# Write a python script to display the number of days in a given month number
a=int(input("enter a month name:"))
match a:
    case a if a in (1,3,5,7,8,10,12):
        print("31 days")
    case a if a in (4,6,9,11):
        print("30 days")
    case 2:
        print("28 days or 29 days")
    case a:
        print("enter valid month number")
    
