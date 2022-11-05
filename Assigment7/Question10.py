"""10. Write a program to display day name on the basis of user’s liking of a colour. Ask
      user for his favorite colour. User can answer in a sentence like “I like red colour”.
      Assuming all colour name entered by user is in lowercase. Use match case to display
      day name associated with the colour.
      a. Yellow - Monday
      b. Blue - Tuesday
      c. Orange - Wednesday
      d. White - Thursday
      e. Black - Friday
      f. Red - Saturday
      g. All other colours - Sunday"""
s1=input("what is your favourite color ")
l1=["yellow","blue","orange","white","black","red"]
for color in l1:
    if color in s1:
        c=color
        break
    else:
        c="other"
    match c:
        case "yellow":
            print("Monday")
        case "blue":
            print("tuesday")
        case "orange":
            print("wednesday")
        case "white":
            print("thrusday")
        case "black":
            print("friday")
        case "red":
            print("saturday")
        case "others":
            print("sunday")
            
