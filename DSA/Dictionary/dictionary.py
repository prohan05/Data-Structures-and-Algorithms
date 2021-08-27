

def traversedict(dicto):
    for key in dicto:
        print(dict, dicto[key])


def searchdict(dicto, value):
    for key in dicto:
        if dicto[key] == value:
            return key, value
    return "The value doesn't exist"


def delete(dicto, value):
    dicto.pop() # Removes the key and return key if asked
    dicto.popitem() # Removes key but return key and value
    dicto.clear() # Deletes whole dictionary
    # u can use 'del parameter'

# Dictionary Method