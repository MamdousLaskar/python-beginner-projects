print('Welcome to my computer quiz!')

playing = input('Do you want to play? ').lower()

if playing != 'yes':
    quit()

print('Lets Play :) \n')

score = 0
question = 0

answer = input('''What does CPU stand for?
a.Core Power Unit  b.Central Processing Unit  c.Core Power Unit  d.Car Pressure Unit\n''').lower()

if answer == 'central processing unit' or answer == 'b':
    print('Correct!\n')
    score += 1
    question += 1
else:
    print('Incorrect!\n')


answer = input('What does GPU stands for?\na.Grahics Processing Unit   b.Graphical Processing Unit  c.Gear Pressure Unit  d.NONE\n').lower()
if answer == 'graphics processing unit' or answer == 'a':
    print('Correct!\n')
    score += 1
    question += 1
else:
    print('Incorrect!\n')


answer = input('What does RAM stand for?\na.Read Allocated Memory   b.Random Access Memory  c.Reload Access Memory  d.Read Available Memory\n').lower()

if answer == 'random access memory' or answer == 'b':
    print('Correct!\n')
    score += 1
    question += 1
else:
    print('Incorrect!\n')


answer = input('What does ALU stand for?\na.Arithmetic Logical Unit   b.Allocated Large Unit c.Access Logical Unit  d.Assistant Language Unit\n ').lower()

if answer == 'arithmetic logical unit' or answer == 'a':
    print('Correct!\n')
    score += 1
    question += 1
else:
    print('Incorrect!\n')


answer = input('What does AI stand for?\na.Arithmetic Induction  b.Allocated Integers  c.Both a & b  d.Artificial Intelligence\n').lower()

if answer == 'arithmetic logical unit' or answer == 'd':
    print('Correct!\n')
    score += 1
    question += 1
else:
    print('Incorrect!\n')

print(f'You got {question} correct!  Your score is {score * 10} out of 50')
print(f'You got {(score / 5) * 100}%')


