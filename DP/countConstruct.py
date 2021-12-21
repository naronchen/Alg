def countConstruct(target, wordBank, d={}):
    if target in d: return d[target]
    if target == "": return 1

    count = 0
    for word in wordBank:
        if target[0:len(word)] == word :
            numWays = countConstruct(target[len(word):], wordBank)
            count += numWays
    
    d[target] = count
    return count


print(countConstruct("abc", ["a", "b", "g", "c"]))
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(countConstruct("skateboard", ["bo", "rd", "ate", "ska", "sk", "boar"]))
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeef", ["e","ee","eee","eeee","eeeee","eeeeee", "eeeeeeeef"]))
