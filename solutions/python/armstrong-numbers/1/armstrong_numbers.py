def is_armstrong_number(number):
    number_str = str(number)
    number_len = len(number_str)

    total = sum(int(char) ** number_len for char in number_str)

    return number == total