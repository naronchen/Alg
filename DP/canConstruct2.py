def canConstruct(target, wordBank):
    l = len(target) + 1
    t = l * [False]
    t[0] = True

    for i in range(l):
        if t[i] is True:
            for word in wordBank:
                if target[i: i+len(word)] == word:
                    t[i + len(word)] = True
    return t[-1]

print(canConstruct("abc", ["a", "b", "g", "c"]))
print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canConstruct("skateboard", ["bo", "rd", "ate", "ska", "sk", "boar"]))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeef", ["e","ee","eee","eeee","eeeee","eeeeee", "eeeeeeeef"]))