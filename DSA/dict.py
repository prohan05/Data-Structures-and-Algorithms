
"""
sal = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(sal.get('d', "not found"))
print(sal.get('e', "not found"))
print(sal.keys())
print(sal.values())

print("Key-Value pair")
for k, v in sal.items():
    print("The key is ", k, "the value is", v)

print("Highest value   " + max(sal, key=sal.get))
print("Lowest value    " + min(sal, key=sal.get))

print(sal.popitem())
print(sal)

print(sal.pop('b'))
print(sal)
"""
"""
eng = {}

eng['solitude'] = ['lone', 'lonely', 'alone', 'unaccompanied']
eng['hope'] = ['aspiration', 'desire', 'wish', 'ambition']
print(eng)

eng.clear()
eng = {'solitude': []}
eng_w = ['lone', 'lonely', 'alone']
eng['solitude'].append(eng_w[0])
print(eng)
eng['solitude'] = eng_w
print(eng)

if eng.get('solitude'):
    for item in eng['solitude']:
        print(item)
else:
    print('word not found')
"""
""""
keys = ['a', 'b', 'c']
values = [1, 2, 3]

print('keys are: ' + str(keys))
print('values are: '+ str(values))

sal = {}
print('#Method 1#')
index = 0
for key in keys:
    value = values[index]
    sal[key] = value
    index += 1

print('DICTIONARy made: ', str(sal))
"""
# Dict using comprehension
keys = ['a', 'b', 'c']
values = [1, 2, 3]
sal = {keys[index]: values[index] for index in range(0, len(keys))}
print(sal)
# conditional
sal_grt3 = {keys: values for keys, values in sal.items() if values > 1}
print(sal_grt3)
