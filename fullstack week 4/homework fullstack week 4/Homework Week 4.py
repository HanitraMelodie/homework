"""
Two Sum
-------------------------------------------------------------------------------------------------------------------------
Given an array of integers nums and an integer target, return two numbers inside that array such that they add up to target.

You may assume that each input would have at least one solution, and you may not use the same element twice.

You can return the answer in any order.

EXAMPLE 1:
---------------------------------------------------------------
Input: nums = [2,7,11,15], target = 9
Output: [2, 7]
Explanation: Because nums[0] + nums[1] == 9, we return [2, 7].

EXAMPLE 2:
---------------------------------------------------------------
Input: nums = [3,2,4], target = 6
Output: [2, 4]

EXAMPLE 3:
---------------------------------------------------------------
Input: nums = [3,3], target = 6
Output: [3, 3]

NOTES:
---------------------------------------------------------------
- An input MAY HAVE no two numbers at all (an empty one still counts as a solution) - in this case, return a empty array
- It's an array of integer numbers - these numbers are not necessarily distinct / unique
- Make sure to discuss your solution - what is the Big O Time & Space complexity? Was there anyway you could've done...
...better or not? Why or why not? Justify.
"""

#----------------STARTING CODE PACK------------------------------------------------------------------------------------------
#Back to the foundation assessment, we had a similar coding challenge.
#The code below was my answer to the coding challenge
#

#definition variables

# numbers=[5, 3, -4, -5, 11, 1, -1, 6]
# target=10
#
# #definition function with two loops
# def TwoSum(numbers,target):
#         for i in range(0, 8):
#             number1=numbers[i]
#             for j in range(1, 8):
#                 number2 = numbers[j]
#                 #sum of any number in the array which could be the target
#                 sum_number = number1 + number2
#                 #comparison of each sum to the target
#                 if sum_number == target:
#                 #creation of a list to store the solution
#                  my_list = []
#                  my_list.append(number1)
#                  my_list.append(number2)
#                  print(my_list)
#                  return True
#         #if there is no solution , the list is sent empty
#         my_list = []
#         print(my_list)
#         return False
#
# TwoSum(numbers,target)


#---------------------IMPROVED CODE--------------------------
#As we continuously learn more about Python, I can see now that my previous code could be more efficient.
#
# #definition of variables
numbers = [5, 3, -4, -5, 11, 1, -1, 6]
target = 10
#make the range more mutable
rangearray = len(numbers)
#
# #definition function
def TwoSum(numbers, target):
    #incrementation of loops instead of a loop then another loop
    for i in range(0, rangearray):
        for j in range(i+1, rangearray):
            #add the condition i is different from j and remove the creation of sum_number variable to compare directly the sum of numbers[i] numbers[j] with the target
            if i != j and numbers[i] + numbers[j] == target:
            # removing the double use of append to store the solution in the array
                my_list = [numbers[i], numbers[j]]
                print(my_list)
                return True
    my_list = []
    print(my_list)
    return False
TwoSum(numbers,target)

#---------------------------------INTERVIEW QUESTIONS--------------------------------
#what is the Big O Time & Space complexity?
#the Big O Time & Space complexity is a measure to determine the efficiency of our algorithm.
# The complexity analysis is to define the time and space complexity of an algorithm

#Calculation of the time complexity of my code above:
#we have i =N, it  will run N times
#we have j=I+1=N+1 , it will run N+1 times
#so the time complexity is egal to N+ N+1 =2N+1
# the code above is O(n^2) time complexity

#Calculatation of the space complexity of my code above:
#we have i =N, it  will run N times
#we have j=I+1=N+1 , it will RUn N+1 times
#we have two variables j and i
#the space complexity is N*C +(N+1)*c +1*c +1*c = NC + NC+ C+C+C= 2NC+ 3C =where c is a unit space taken
# the code above is O(n) space complexity

#Was there anyway you could've done better or not? Why or why not? Justify.
#the space complexity is quite good  but the time complexity is not efficient,
# it is actually one of the worst case but the coding challenge is quite complex itself.
#To reduce the time complexity, one of the most efficient solution would be to remove any nested loop. I learnt from
#this source https://builtin.com/job-interviews/solve-two-sum-problem that there is a way to remove the nested loop
#using a python dictionnary.
