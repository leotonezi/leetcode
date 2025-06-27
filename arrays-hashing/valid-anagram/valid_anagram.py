def valid_anagram(s: str, t: str):
    if len(s) != len(t):
        return False

    # Count frequencies in s
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Subtract frequencies based on t
    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False

    return True
