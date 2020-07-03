basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print('orange' in basket)
print('crabgrass' in basket)


a = set('abracadabra')
b = set('alacazam')


print(sorted(a))
print(sorted(a - b))
print(sorted(a | b))
print(sorted(a & b))
print(sorted(a ^ b))
