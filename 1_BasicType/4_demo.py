

def convertListToString(list):
    # convert a list to string, split by ',', last element append by 'and'
    beforeLast = list[:len(list)-1]
    split = ','
    result = split.join(beforeLast)
    result += ' and ' +  list[len(list)-1]
    return result

result = convertListToString(['apples', 'bananas', 'tofu', 'cats', 'watermelon'])
print(result)