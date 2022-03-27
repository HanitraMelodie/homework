
#Question 3
from random import randint
#the winning ticket
lotteryticketwinner = [29,5,7,35,23,17,1]
#lottery ticket generator
lotteryticketrandom = [randint(0, 49) for i in range(7)]
#search for the matches between the winning ticket and the generated ticket
lotterymatch = set(lotteryticketrandom)&set(lotteryticketwinner)
print('Matching number {}'.format(lotterymatch))
#count the number of matches between the winning ticket and the generated ticket
matchingnumber = len(lotterymatch)
#check if the matches between the winning ticket and the generated are enough to win money
if 0 <= matchingnumber < 3:
    print('Sorry, you lost')
if matchingnumber == 3:
    print('Congratulations, you just won £20')

if matchingnumber == 4:
    print('Congratulations, you just won £40')

if matchingnumber == 5:
    print('Congratulations, you just won £100')

if matchingnumber == 6:
    print('Congratulations, you just won £100000')

if matchingnumber == 7:
    print('Congratulations, you just won £1000000')