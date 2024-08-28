def is_anagram(str1: str, str2: str):
    count_str1, count_str2 = {}, {}
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        count_str1[str1[i]] = 1 + count_str1.get(str1[i], 0)
        count_str2[str2[i]] = 1 + count_str2.get(str2[i], 0)
    for c in count_str1:
        if count_str1[c] != count_str2.get(c, 0):
            return False
    return True


print(is_anagram("anagram", "margana"))
print(is_anagram("car", "rat"))
