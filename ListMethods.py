fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print("Apples are: " ,fruits.count('apple'))

print("Tangerines are: ", fruits.count('tangerine'))

print("Fruit Index Banana: ", fruits.index('banana'))

print("Fruit Index Banana starting a position 4: ", fruits.index('banana', 4))

fruits.reverse()
print("Fruit Reverse: ",fruits)

fruits.append('grape')
print("Fruit Append Grape: ",fruits)

fruits.sort()
print("List Sorted: ",fruits)

print("POP: ",fruits.pop())
