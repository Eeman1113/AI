print("hello")
name=input("what is your name:")
print("hey ",name)
ans=input("would you like to talk with me:")
if ans=='yes':
	print(" ok lets talk")
	ques=input("ask me a question:")
	if ques=='who are you':
		print("I am M.O.N.K.E.Y")
	elif ques=='where do you live':
		print("in Eeman's device")
	elif ques=='how old are you':
		print('I AM JUST 1 DAY OLD (•_•)')
	elif ques=='what are you doing':
		print("I am Talking to you")
	elif ques=='what are you eating':
		print("yumm! pie:-)")
	elif ques=='mario':
		print("letss go!!")
		print("(＾∇＾)")
		print('''─▄████▄▄░
▄▀█▀▐└─┐░░
█▄▐▌▄█▄┘██
└▄▄▄▄▄┘███
██▒█▒███▀''')
elif ans=='no':
	print("ok see you next time")
elif ans=='exit':
    exit()