def reverse_integer(x: int):
    min_signed_64bit = -2**31 - 1
    max_signed_64bit = 2**31 - 1

    stringed_number = str(x)
    negative = True if stringed_number[0] == "-" else False

    reverse_string = stringed_number[::-1] if not negative else stringed_number[:0:-1]

    converted_number = int(reverse_string) if not negative else int(reverse_string) * -1



    if not min_signed_64bit < converted_number < max_signed_64bit:
        #"Error: number not in the range of a Signed 32-bit."
        return -1

    return converted_number


print(reverse_integer(-495))
