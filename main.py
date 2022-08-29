import random
import os
from data import data ,n
from art import logo , vs

def details(index):
    return f"{data[index]['name']}, {data[index]['description']}, from {data[index]['country']}"
def compare(num1 , num2):
    if data[num1]['follower_count'] > data[num2]['follower_count']:  # follower count comparision
        return 'A'
    else:
        return 'B'




print("Welcome to higher , lower game ")
print(logo)
index1 = random.randint(0,n+1)   # index number for list members
end_game = False
score=0
while not end_game:
    print(f"Compare A : {details(index1)}")
    index2 = random.randint(0,n+1)
    print(vs)
    print(f"Against B : {details(index2)}")
    ans = input("Who has more followers ? Type 'A' or 'B' ")
    if ans==compare(index1,index2):         # pass indexes to function to compare number of followers
        os.system('clear')
        score+=1
        print(f'You are right , Your current score {score}')
        index1=index2
    else:
        os.system('clear')
        print(f"Sorry ,  that's wrong. Final score {score}")
        end_game = True

