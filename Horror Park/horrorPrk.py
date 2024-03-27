name = input("Type your name: ")
print("welcome",name, "to this Horror Park!")

answer = input("You are on Horror Road, it has come to an end and you can go left or right. Which way would you like to go? : ").lower()

if answer == 'left':
    answer = input("You come to a Haunted house, you can go in or back to Horror road :) ? type dare to go alone in and dumb to go with friends : ")
    
    if answer == 'dare':
     print("Hii.. Hii.. you roast and eaten by Ghost ! \n You loose!") 
    elif answer == 'dumb':
     print("Hua.. Hua.. all are hanged by Ghost !\n You loose!")
    else :
     print("not a valid option. You Died!")

elif answer == 'right':
    answer = input("You come to a Black haunted forest, you can go in or back to Horror road :) ? type cross to go alone in and back to go back : ")

    if answer == 'cross':
     answer = input("Hooo... you cross forest bravely, now meet a stranger. Do you wanna talk (yes/no)? : ") 
     if answer == 'yes':
       print("Hurray! He is a priest.. he saves you..\n YOU WON! :)")
     elif answer == 'no':
       print("Wua.. Wua.. you ignore him they offended and attack on you..\n You loose! :(")
     else:
      print("not a valid option. You Died!")
       
    elif answer == 'back':
     print("You coward ! \n Go to hell.. You loose!")
    else :
     print("not a valid option. You Died!")
else:
    print("not a valid option. You Died!")