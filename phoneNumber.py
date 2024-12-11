phone_number = str(input("Write your number here: "))
special_chars = [" ", "(", ")", "-"]

chars = []
for i in phone_number:
    #checks if the charachter is a number and adds it to the list
    if i in special_chars:
        pass
    else:
        if (int(i) or i == "0"):
            chars.append(i)

if (phone_number[0] != "(" or phone_number[4] != ")" or phone_number[5] != " " or phone_number[9] != "-") or len(chars) != 10:
    print("!Number is formatted correctly")
else:
    print("Number is formatted correctly!")