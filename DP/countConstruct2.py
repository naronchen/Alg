def countConstruct(target, wordBank):
    l = len(target) + 1
    t = [0] * l
    t[0] = 1

    for i in range(l):
        if t[i] != 0:
            for word in wordBank:
                if i+len(word) < l :
                    if word == target[i: i+len(word)]:
                        t[i+len(word)] += t[i]

    return t[-1]

print(countConstruct("abc", ["a", "b", "g", "c"]))
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef"]))
print(countConstruct("skateboard", ["bo", "rd", "ate", "ska", "sk", "boar"]))
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeef", ["e","ee","eee","eeee","eeeee","eeeeee", "eeeeeeeef"]))