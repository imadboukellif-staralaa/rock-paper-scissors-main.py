import random
print ('welcome to the rock paper scissours game ')
help=input('press enter to continue or type help for tje rules help').lower()
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
if help=="help":
	print("""
********* RULES *********
1) You choose and the computer chooses
2) Rock smashes Scissors -> Rock wins
3) Scissors cut Paper -> Scissors win
4) Paper covers Rock -> Paper wins
""")
choice=input('Enter your choice (rock, paper, scissors):       ').lower()
computer_choice=random.choice(['rock','paper','scissors'])
if choice==computer_choice:
	print('no win')
elif choice =='paper' and computer_choice=='rock':
	print('youuuuuuuuuuu winer but your choice is :')
	print(paper)
	print('and computer choice:')
	print(rock)
elif choice=='rock' and computer_choice=='scissors':
	print('youuuuuuuuuuuuuuuu winnneer but your choice is:')
	print(rock)
	print('but the computer choice is :')
	print(scissors)
elif choice== "scissors"and computer_choice=='paper':
	print('youuuuuuuu winnnnnner but your choice is :')
	print(scissors)
	print('and computer choice : ')
	print(paper)
elif computer_choice=='rock' and choice=='scissors':
	print ('compuuuuuuter winnner but your choice is :')
	print(scissors)
	print("and computer choice is :")
	print(rock)
elif computer_choice=='scissors' and choice=='paper':
	print ('compuuuuuuter winnner but your choice is :')
	print(paper)
	print('and computer choice is :')
	print(scissors)
elif computer_choice=='paper' and choice=='rock':
	print ('compuuuuuuter winnner but your choice is :')
	print(rock)
	print('and computer choice is : ')
	print(paper)
else :
	print('invaliable choice')
	

