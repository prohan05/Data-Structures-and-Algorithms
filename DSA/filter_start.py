# Using a hash table to filter the duplicates
# O(n)

items = [1, 1, 2, 1, 2, 6, 4, 2, 5, 7, 5, 4, 3, 5, 6, 4, 2, 4, 5, 6, 4, 3]
"""
filter = dict()

for key in items:
    filter[key] = 0

result = set(filter.keys())
print(result)

"""
# counting duplicates

counter = dict()

for key in items:
    if key in counter.keys():
        counter[key] += 1
    else:
        counter[key] = 1

print(counter)


