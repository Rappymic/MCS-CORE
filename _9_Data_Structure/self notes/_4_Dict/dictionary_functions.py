dict1 = {'a': 23, 'b': 34, 'c': 45}
dict2 = {'d': 434, 'e': 332, 'f': 98}
print("Adding data".center(80, "-"), "\n")
print("Original Dictionary".ljust(40, "-"), dict1)
del dict1['b']
print("after element update".ljust(40, "-"), dict1)
dict1['g'] = 82
print("adding element".ljust(40, "-"), dict1)
print(f"the value of 'a' key is".ljust(40, "-"), dict1['a'])
dict1['a'] = "test"
dict3 = dict1.copy()
print(f"update the value of 'a'".ljust(40, "-"), dict1)
dict1.clear()
print("clearing the dictionary".ljust(40, "-"),dict1)
del dict1
try:
    print("Deleted dictionary", dict1)
except Exception as e:
    print("Dictionary is deleted and", e)

print("dictionary methods".center(80, "-"))
print("dictionary .keys function".ljust(40, "-"), dict3.keys())
print("dictionary .values function".ljust(40, "-"), dict3.values())
print("updating the dictionary with two dictionaries".center(80, "-"))
print("dictionary 1".ljust(40, "-"), dict3)
print("dictionary 2".ljust(40, "-"), dict2)
dict3.update(dict2)
print(f"{dict3}".center(70))
print("Retrieving values".center(80, "-"))
print("getting value of a ".ljust(40, "-"), dict3.get('a'))
print("getting value of an absent key ".ljust(40, "-"), dict3.get(1))
print("set default function".center(80, "-"))
print("checking if a is present ".ljust(40, "-"), dict3.setdefault("a","testing"))
print("checking if T is present ".ljust(40, "-"), dict3.setdefault("T","testing"))
print(dict3)