"""
Algorithms 1 Solution
-------------------------------------------------------------------------------------------------------------------------
"""
#
# def isValidSubsequence(array, sequence):
#     i = 0
#     for number in array:
#         if i == len(sequence):
#             break
#         if sequence[i] == number:
#             i += 1
#
#     return i == len(sequence)
#
# array1 = [5,1,22,25,6,-1,8,10]
# sequence1 = [1,6,-1,-2]
# length = len(array1)
# length2 = len(sequence1)
# print(isValidSubsequence(array1, sequence1))
#
# array2 = [5,1,22,25,6,-1,8,10]
# sequence2 = [1,6,-1, 10]
# print(isValidSubsequence(array2, sequence2))
#
# array3 = [5,1,22,25,6,-1,8,10]
# sequence3 = [25]
# print(isValidSubsequence(array3, sequence3))

"""
Algorithms 2 Solution
-------------------------------------------------------------------------------------------------------------------------
"""

def findThreeLargestNumbers(array):
    array = sorted(array)
    tries = 0
    count = 1

    for i in range(1, n + 1):
        if (count <=3):
            if (tries != array[n - i]):
                print(array[n - i])
                tries = array[n - i]
                count += 1
        else:
            pass




array= [141, 1, 17, -17, -27, 18, 541, 8, 7, 7]
n = len(array)
expectedOutput1 = [18, 141, 541]
print(str(findThreeLargestNumbers(array)) + " <-- --> " + str(expectedOutput1))  # [18, 141, 541]

# array= [141, 1, 214, -17, -27, 0, 541, 21, 7, 34]
# n = len(array)
# expectedOutput2 = [141, 214, 541]
# print(str(findThreeLargestNumbers(array)) + " <-- --> " + str(expectedOutput2))  # [141, 214, 541]

