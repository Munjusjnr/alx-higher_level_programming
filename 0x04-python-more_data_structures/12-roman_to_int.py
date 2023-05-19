#!/usr/bin/python3
def roman_to_int(roman_string):
    num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    results = 0
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    for i, c in enumerate(roman_string):
        if (i + 1) == len(roman_string) or num[c] >= num[roman_string[i + 1]]:
            results += num[c]
        else:
            results -= num[c]
    return results
