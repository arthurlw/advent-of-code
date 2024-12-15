left = []
right = []

while True:
    try:
        line = input()
        if line.strip() == "":
            break
        numbers = list(map(int, line.split()))
        left.append(numbers[0])
        right.append(numbers[1])
    except:
        break

similarity = []

num = 0
i = 0
j = 0

while True:
    if i + 1 > len(left) or j + 1 > len(right):
        break
    if sorted(left)[i] > sorted(right)[j]:
        j += 1
        similarity.append(num)
        num = 0
    elif sorted(left)[i] < sorted(right)[j]:
        i += 1
    else:
        while sorted(left)[i] == sorted(right)[j] and j - 1 < len(right):
            num = num + sorted(left)[i]
            j += 1
        similarity.append(num)
        num = 0
print(sum(similarity))