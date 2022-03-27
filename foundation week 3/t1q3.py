#Question3
import math
year=input("Which year has the book been written?")
centuryconversion= int(year)/100
century=math.floor(centuryconversion)
print('{}th Century'.format(century))
