import math
class BaseConverter:
    def __init__(self, decimal_value:int):
        self.decimal_value = decimal_value

    def to_any_base(self, number_of_digits:int, specific_base:int) -> tuple:
        digit_list = []
        while self.decimal_value > 0:
            digit_list.append(self.decimal_value%specific_base)
            self.decimal_value = math.floor(self.decimal_value/specific_base)
        while len(digit_list) < number_of_digits:
            digit_list.append(0)
        if len(digit_list) > number_of_digits:
            raise ValueError("resulting number's number of digits exceeds given number of digits!")
        digit_list.reverse()
        return tuple(digit_list)

    @staticmethod
    def tuple_to_decimal_value(given_tuple:tuple, base:int) -> int:
        value = 0
        exponent = len(given_tuple) - 1
        for digit in given_tuple:
            value+=digit*(base**exponent)
            exponent-=1
        return value