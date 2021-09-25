name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on dirt road, it has come to an end you can go left or right. Wich way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, You can walk around it or swim accross? type wlak to walk around and swim to swim acrross: ")
    if answer == "swim ":
        print("You swim acrross and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, run out of the water and you lost the game.")
    else:
        print("Not a valid option, You lose.")


elif answer == "right":
    answer = input("You come to bridge, it looks wobbly, do you want to cross it or head back (sross/back)? ")

    if answer == "back ":
        print("You go back or lose. ")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger, do you talk to them (yes/no)? ")

    if answer == "Yes":
        print("You talk to the stranger and they give you gold. You win!")

    elif answer== "No":
        print("you ignore the stranger and they are o ffended, then you lose ")

    else:
        print("Not a valid option, You lose.")
else:
     print("Not a valid option, You lose. ")

print("Thank you for trying", name)
