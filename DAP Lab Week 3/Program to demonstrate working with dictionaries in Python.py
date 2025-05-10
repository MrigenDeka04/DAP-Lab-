my_dict = {}
print("Empty dictionary is:", my_dict)
my_dict = {1: 'apple', 2: 'ball'}
print("dictionary with integer keys", my_dict)
my_dict = {'name': 'rishi', 1: [2, 4, 3]}
print("dictionary with mixed keys", my_dict)
my_dict = dict.fromkeys("abcd", 'alphabet')
print("dictionary created by using dict.fromkeys method =", my_dict)
my_dict = {'name': 'jack', 'age': 25}
print(my_dict['name'])
my_dict['age'] = 18
my_dict['class'] = "B.Tech"
print("After changing and adding the values, the new dictionary =", my_dict)
print("items in the dictionary is:", my_dict.items())
print("Keys in the dictionary is:", my_dict.keys())
print("values in the dictionary is:", my_dict.values())