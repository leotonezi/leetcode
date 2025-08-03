def checkInclusion(s1, s2):
    counter = dict()
    for i in list(s1):
        if i not in counter:
            counter[i] = 0
        counter[i] += 1

    window_size = len(s1)
    x = 0
    while x <= len(s2) - window_size:
        temp_counter = counter.copy()
        for i in range(window_size):
            if s2[x + i] in temp_counter.keys():  # Use x + i
                temp_counter[s2[x + i]] -= 1
        if all(value == 0 for value in temp_counter.values()):
            return True
        x += 1
    return False
