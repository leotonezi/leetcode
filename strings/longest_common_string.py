def longestCommonPrefix(strs):
    if not strs:
        return ""

    result = ""

    for i in range(len(strs[0])):
        char = strs[0][i]

        for text in strs:
            if i >= len(text) or text[i] != char:
                return result

        result += char

    return result
