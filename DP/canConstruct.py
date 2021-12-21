# def canConstruct(target, wordBank):
#     if target == "": return True
#     if target in wordBank: return True

#     for word in wordBank:
#         count = 0
#         for i in range(len(word)):
#             if i < len(target) and word[i] == target[i]: 
#                 count += 1

#         if count == len(word): 
#             if canConstruct(target[len(word):], wordBank) is True: return True

#     return False

def canConstruct(target, wordBank, d={}):
    if target in d: return d[target]
    if target == "": return True
    if target in wordBank: return True

    for word in wordBank:
        if target[0:len(word)] == word :
            if canConstruct(target[len(word):], wordBank, d): 
                d[target] = True
                return True

    d[target] = False
    return False

print(canConstruct("abc", ["a", "b", "g", "c"]))
print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canConstruct("skateboard", ["bo", "rd", "ate", "ska", "sk", "boar"]))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeef", ["e","ee","eee","eeee","eeeee","eeeeee", "eeeeeeeee"]))
