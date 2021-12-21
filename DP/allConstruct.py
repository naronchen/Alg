from copy import deepcopy

def allConstruct(target, wordBank, d = {}):
    if target in d: return d[target]
    if target == "": return [[]]
    
    ways = []

    for word in wordBank:
        
        if target[:len(word)] == word:
            result = allConstruct(target[len(word):], wordBank,d)
            for way in result:
                ways.append(way + [word])
    
    d[target] = ways
    return ways



print(allConstruct("abc", ["a", "b", "g", "c"]))
print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(allConstruct("skateboard", ["bo", "rd", "ate", "ska", "sk", "boar"]))
print(allConstruct("purple", ["purp", "p", "ur", "le","purpl"]))
print(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeef", ["eeee","eeeee","eeeeee", "eeeeeeeef"]))
