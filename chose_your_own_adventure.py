name = input('Enter your name: ')
print('Welcome', name, 'to this adventure!\n')

answer = input('You are on a dirt road, it has come to and end and you can go left or right, which way would you like to go?\nEnter left for going left and right for going right\n').lower()

if answer == 'right':
	answer = input('You come to a river, you can walk around it or swim across, Which would you choose?\nEnter walk or swim\n').lower()
	if answer == 'walk':
		answer = input('You walked about five miles and you are very tired, you find a hostel for resting. Would you like to checkout the hostel.\nEnter yes or no\n').lower()
		if answer == 'yes':
			print('You stayed in the hostel and after some time started snowing. You stayed there and left the hostel next moring.\n')

		elif answer == 'no':
			print('You started walking and walked around another five miles, you are very hungry. Suddenly started  snowing and you see no one and after after a while the whole place bocome white and due to low visibility you fall into a long pit and you die!\nYou lose!')

		else:
			print('Not a valid option. You lose!')

	elif answer == 'swim':
		print('This river has crocodiles and they ate you, you die.\nYou lose ')

	else:
		print('Not a valid option. You lose!')

elif answer == 'left':
	print('You go to the left')

else:
	print('Not a valid option. You lose!')