# Task 3.1

"""chairs=15
nails=4
total_nails=chairs*nails
message='I need to buy {} nails'.format(total_nails)
print(message)
"""
#task 3.2
"""my_name='Penelope'
my_age=29

message='My name is {} and I am {} years old'.format(my_name,my_age)
print(message)
"""

#task 3.3
"""box=input("how many boxes of eggs do you have ? ")
eggs=6
box_eggs = float(box) * float(eggs)
omelettes= float(box_eggs)/4
message='you can make {} omelettes with {} boxes of eggs'.format(omelettes,box)
print(message)"""

#task 3.Q4.1
"""my_str="I love coding."
my_str=my_str.replace(".","!")
print(my_str)"""

#task 3.Q4.2
"""my_str_1="EVERY Exercise Brings Me CLoser to Completing my GOALS"
my_str_1=my_str_1.lower()
print(my_str_1)"""

#task 3.Q4.3
"""my_str_2="We enjoy travelling"
ans_1=my_str_2.startswith('A')
print(ans_1)"""

#Task 3.Q4.4
"""my_str_3="1.458.001"
ans_2=len(my_str_3)
print(ans_2)"""

#task 3.Q5.1
"""wrd="Python"
ans_1=wrd[2:6]
print(ans_1)"""
#task 3.Q5.2
"""wrd="Python"
ans_1=wrd[0:4]
print(ans_1)"""
#task3.Q5.3
"""wrd="Python"
ans_1=wrd[2:4]
print(ans_1)"""
#task 5.Q3.4
"""wrd="Python"
ans_1=wrd[2:5:2]
print(ans_1)"""
#task3.Q6
"""for number in range(100):
    output='o'*number
print(range(100))
print(output)"""

#Task3.Q7
def calculate_vat(amount):
    q=amount * 1.2
    return q
#outside function
total=calculate_vat(100)
print(total)

#task 3.q8
"""item_1_name=input("what is the first article ? ")
item_1_price = input("what is the price of first article ? ")
item_2_name=input("what is the first article ? ")
item_2_price = input("what is the price of second article ? ")
item_3_name=input("what is the third article ? ")
item_3_price = input("what is the price of third article ? ")

total = float(item_1_price)+float(item_2_price)+float(item_3_price)
message1 ='{}........{}'.format(item_1_name,item_1_price)
message2 ='{}........{}'.format(item_2_name,item_2_price)
message3 ='{}........{}'.format(item_3_name,item_3_price)
message4 ='Total.....{}'.format(total)
print(message1)
print(message2)
print(message3)
print(message4)
"""
