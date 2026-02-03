def minCost(str1, str2):
    n = len(str1)
    diff = []
    for i in range(n):
        if str1[i] != str2[i]:
            diff.append(i)
    if not diff:
        return 0
    res = 0
    i = 0
    while i < len(diff) - 1:
        if diff[i+1] - diff[i] == 1:
            res += 1
            i += 2
        else:
            res += 2
            i += 1
    if i < len(diff):
        res += 1
    return res


str1 = input("Enter string 1 :")
str2 = input("Enter string 2 :")
print(min is)
print(minCost(str1, str2))
