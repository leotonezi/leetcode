def daily_temperatures(temperatures):
    n = len(temperatures)
    result = [0] * n
    stack = []

    for i in range(n):
        # While stack is not empty and current temp is warmer than stack top
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index

        stack.append(i)

    return result


# Test cases
temperatures1 = [73, 74, 75, 71, 69, 72, 76, 73]
print(daily_temperatures(temperatures1))  # [1,1,4,2,1,1,0,0]

temperatures2 = [30, 40, 50, 60]
print(daily_temperatures(temperatures2))  # [1,1,1,0]

temperatures3 = [30, 60, 90]
print(daily_temperatures(temperatures3))  # [1,1,0]
