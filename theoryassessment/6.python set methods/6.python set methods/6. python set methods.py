#add
"""thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)"""

#clear
"""fruits = {"apple", "banana", "cherry"}

fruits.clear()

print(fruits)"""

#copy
"""fruits = {"apple", "banana", "cherry"}

x = fruits.copy()

print(x)"""

#difference
"""x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)

print(z)"""

#intersection
"""x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)"""

#issubset
"""x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)"""

#issuperset
"""x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)"""

#pop
"""fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)"""
#remove
"""fruits = {"apple", "banana", "cherry"}

fruits.remove("banana")

print(fruits)"""

#symmetricdifference
"""x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)"""

#union
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)

print(z)