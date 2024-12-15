safety = []
while True:
    user_input = str(input())
    if user_input == "":
        break
    user_input = list(map(int, user_input.split()))
    safety.append(1)

    decreasing = user_input[0] > user_input[1]

    for i in range(len(user_input) - 1):
        if decreasing:
            if abs(user_input[i] - user_input[i + 1]) > 3 or user_input[i] <= user_input[i + 1]:
                safety.pop()
                safety.append(0)
                break
        else:
            if abs(user_input[i] - user_input[i + 1]) > 3 or user_input[i] >= user_input[i + 1]:
                safety.pop()
                safety.append(0)
                break

print(sum(safety))
