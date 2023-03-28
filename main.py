N = 5
S = 'abaab'

f = {}
for idx,ch in enumerate(S):
    if ch not in f:
        f[ch] = []

    f[ch].append(idx)

output = 1

for key,value in f.items():
    output = output * len(value)

output += N

print(output)