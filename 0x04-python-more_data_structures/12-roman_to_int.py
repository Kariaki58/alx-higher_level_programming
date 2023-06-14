#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    mapper = ["I", "V", "X", "L", "C", "D", "M"]
    values = [1, 5, 10, 50, 100, 500, 1000]
    number = 0
    counter = 0
    for i in roman_string:
        if (i == "I" or counter) and "IX" in roman_string:
            counter = 1
            if i == "X":
                number = number + 9
            continue
        else:
            index_count = mapper.index(i)
            number = number + values[index_count]
    return number
