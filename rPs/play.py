import random

def role():
    user = input("What's your choice...?\n'r' for Rock, 'p' for Paper, 's' for Scissors\n")
    sam = random.choice(['r','p','s'])
     
    if user == sam:
        return 'It\'s is tie'
    
    if win(user,sam):
        return 'You Won!'
    
    return 'You Loose!'

    

    # you will win when --> you choose 'r' and com choose 's' or you choose 's' and com choose 'p' or you choose 'p' and com choose 'r'
def win(you,com):
    if (you == 'r' and com == 's' or you == 's' and com == 'p' or you == 'p' and com == 'r'):
        return True
    

print(role())