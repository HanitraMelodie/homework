from unittest import TestCase
#3.Write a function that can define whether a word is a Palindrome or

def Palindromecheck(word):
    l = len(word)
    print(word)
    if l > 1:
        return word == word[::-1]
    else:
        print('please wirhte a word')
        return False
# print(Palindromecheck('madam'))
# print(Palindromecheck('hanitra'))
# print(Palindromecheck('a'))

#.4Write tests for the newly created Palindrome function. Provide a brief explanation for your test case options.
class TestFunction(TestCase):
     def test_palindromefalse(self):
        expected = False
        result = Palindromecheck(word='hanitra')
        self.assertEqual(expected, result)
     def test_palindrometrue(self):
        expected = True
        result = Palindromecheck(word='anna')
        self.assertEqual(expected, result)
     def test_l(self):
        expected = False
        result = Palindromecheck(word='b')
        self.assertEqual(expected, result)



#9. TWO NUMBER SUM:

#definition variables
# my_number=[5, 3, -4, -5, 11, 1, -1, 6]
# target_sum=10
#
# def sum_up(sum_number):
#         for i in range(0, 8):
#             number1=my_number[i]
#             for j in range(1, 8):
#                 number2 = my_number[j]
#                 sum_number = number1 + number2
#                 if sum_number == target_sum:
#                  my_list = []
#                  my_list.append(number1)
#                  my_list.append(number2)
#                  print(my_list)
#                  return True
#         my_list = []
#         print(my_list)
#         return False
#
# sum_up(10)
# class TestFunction(TestCase):
#     def testsum(self):
#         expected = True
#         result = sum_up(sum_number=5)
#         self.assertAlmostEqual(expected, result)
