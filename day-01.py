ans = 0
numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def is_actual_number(line, p, direction="left"):
    if direction == "left":
        if p - 4 >= 0 and line[p - 4:p + 1] in numbers: return line[p - 4:p + 1]
        if p - 3 >= 0 and line[p - 3:p + 1] in numbers: return line[p - 3:p + 1]
        if p - 2 >= 0 and line[p - 2:p + 1] in numbers: return line[p - 2:p + 1] 
        return False
    else:
        if p + 4 < len(line) and line[p:p + 5] in numbers: return line[p:p + 5]
        if p + 3 < len(line) and line[p:p + 4] in numbers: return line[p:p + 4]
        if p + 2 < len(line) and line[p:p + 3] in numbers: return line[p:p + 3]
        return False

with open('input-01.txt') as f:
    for line in f:
        left, right = 0, len(line) - 1
        while left < right:
            if (line[left].isnumeric() or is_actual_number(line, left)) and (line[right].isnumeric() or is_actual_number(line, right, "right")):
                break
            elif not line[left].isnumeric() and not is_actual_number(line, left): left += 1
            elif not line[right].isnumeric() and not is_actual_number(line, right, "right"): right -= 1
        n1, n2 = is_actual_number(line, left), is_actual_number(line, right, "right") 
        num1 = numbers[n1] if n1 else line[left]
        num2 = numbers[n2] if n2 else line[right]

        number = "".join([str(num1), str(num2)])
        ans += int(number)

print(ans)