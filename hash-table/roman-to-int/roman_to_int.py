
def roman_to_int(roman_string):
    ROMAN_VALUES = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    result = [ROMAN_VALUES[x] for x in roman_string]
    # Apply Roman numeral rules (subtraction when smaller comes before larger)
    total = 0
    for i in range(len(result)):
        # If current value is smaller than next value, subtract it
        if i < len(result) - 1 and result[i] < result[i + 1]:
            total -= result[i]
        else:
            total += result[i]

    return total


print(roman_to_int('LVIII'))
