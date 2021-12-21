def allConstruct(target, wordBank):
    l = len(target) + 1
    t = [[] for i in range(l)]
    t[0] = [[]]

    for i in range(l):
        if t[i] is not []:
            for word in wordBank:
                if target[i: i+len(word)] == word:
                    for way in t[i]:
                        t[i+len(word)].append(way+[word])
    return t[-1]

print(allConstruct("abc", ["a", "b", "g", "c"]))
print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(allConstruct("skateboard", ["bo", "rd", "ate", "ska", "sk", "boar"]))
print(allConstruct("purple", ["purp", "p", "ur", "le","purpl"]))
print(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeef", ["eeee","eeeee","eeeeee", "eeeeeeeef"]))