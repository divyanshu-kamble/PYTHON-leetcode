s = "aaaabbbcccaaaddddee"

result = ""
list[s]
# print(x)
result += s[0]
# print(result)

for i in range(1,len(s)):
    if s[i] != s[i-1]:
        result += s[i]

print(result)
