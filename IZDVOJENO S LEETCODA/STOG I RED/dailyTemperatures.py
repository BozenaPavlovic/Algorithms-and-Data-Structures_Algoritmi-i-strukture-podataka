def dailyTemperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n
    stack = Stack()  # Stog pamti indekse

    for current_day in range(n):
        current_temp = temperatures[current_day]

        # Dok stog nije prazan i današnja temp je veća od temp dana s vrha stoga
        while not stack.is_empty() and current_temp > temperatures[stack.top()]:
            prev_day = stack.pop()
            answer[prev_day] = current_day - prev_day  # Razlika u danima

        stack.push(current_day)

    return answer