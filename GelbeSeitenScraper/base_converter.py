import math
class BaseConverter:
    def __init__(self, decimal_value:int):
        self.decimal_value = decimal_value

    def toBase26(self, number_of_digits:int) -> tuple[int]:
        digit_list = []
        while self.decimal_value > 0:
            digit_list.append(self.decimal_value%26)
            self.decimal_value = math.floor(self.decimal_value/26)
        while len(digit_list) < number_of_digits:
            digit_list.append(0)
        if len(digit_list) > number_of_digits:
            raise ValueError("resulting number's number of digits exceeds given number of digits!")
        digit_list.reverse()
        return tuple(digit_list)