import random

menu = '''
		<===Welcome To Rock Paper Scissors Game===>

Select Option

1. Rock
2. Paper
3. Scissors

Please Select Your Option From 1 to 3
'''

choices = ["Rock","Paper","Scissors"]

print(menu)

p1 = input('Enter Your Option!')

bot_choice = random.choice(choices)

def checks(a,b):
	if (a=='1' and b=='Scissors'):
		return "Player Won"
	elif(a=='2' and b=='Rock'):
		return "Player Won"
	elif(a=='3' and b=='Paper'):
		return "Player Won"
	elif(b=='Rock' and a=='3'):
		return "Bot Won"
	elif(b=='Paper' and a=='1'):
		return "Bot Won"
	elif(b=='Scissors' and a=='2'):
		return "Bot Won"
	else:
		return "Draw"

print(f"Player Choice - {p1}", f"Bot Choice - {bot_choice}")
call = checks(p1,bot_choice)
print(call)