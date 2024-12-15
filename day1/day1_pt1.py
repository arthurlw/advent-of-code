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

diff = []
for i in range(len(left)):
    diff.append(abs(sorted(left)[i] - sorted(right)[i]))
print(sum(diff))