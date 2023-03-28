text1 = "abcdef"
text2 = "abjefi"
st = []

df = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

print(df[0][0])

for i in range(len(text1) -1, -1, -1):
    for j in range(len(text2) - 1, -1, -1):
        if text1[i] == text2[j]:
            df[i][j] = 1 + df[i + 1][j + 1]
            st.append(text1[i])
        else:
            df[i][j] = max(df[i][j + 1], df[i + 1][j])

print(df[0][0])
print(st)
