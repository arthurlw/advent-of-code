def is_safe(report):
    decreasing = report[0] > report[1]
    for i in range(len(report) - 1):
        if decreasing:
            if abs(report[i] - report[i + 1]) > 3 or report[i] <= report[i + 1]:
                return False
        else:
            if abs(report[i] - report[i + 1]) > 3 or report[i] >= report[i + 1]:
                return False
    return True

def is_safe_with_one_removal(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
        if i > 0:
            modified_report = report[:i-1] + report[i:]
            if is_safe(modified_report):
                return True
    return False

safety = []
while True:
    user_input = str(input())
    if user_input == "":
        break
    user_input = list(map(int, user_input.split()))
    if is_safe(user_input) or is_safe_with_one_removal(user_input):
        safety.append(1)
    else:
        safety.append(0)

print(sum(safety))
