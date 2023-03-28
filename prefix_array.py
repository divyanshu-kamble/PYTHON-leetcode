input_array = [1,-1,1,2,-3]
[1,100,-1,1,2,100,-3]
prefix_array = []

for ele in range(len(input_array)):
    if len(prefix_array) == 0:
        prefix_array.append(input_array[ele])

    else:
        v = (prefix_array[ele-1] + input_array[ele])
        prefix_array.append(v)

print(prefix_array)


count = 0

for i in range(len(input_array)):
    if prefix_array[i] == 0 and count == 0:
        count += 1
        input_array.insert(i, 100)

    elif prefix_array[i]==0 and count>=1:

        input_array.insert(i+count, 100)

print(input_array)




















