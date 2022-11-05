"""  Write a menu driven program with the following options:
     a. Check whether a given set of three numbers are lengths of an isosceles triangle or not
     b. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not
     c. Check whether a given set of three numbers are equilateral triangle or not
     d. Exit."""
a=int(input("lenght of first side:-"))
b=int(input("lenght of second side:-"))
c=int(input("lenght of third side:-"))
match a:
     case 1:
          a=b=c
          print("equilateral triangle")

     case 2:
          a=b=c
          print("an isosceles triangle")

     case 3:
          a!=b
          print("right angle triangle")
     case     





