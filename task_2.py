import re
from typing import Callable

number_pattern = r'(?<!\S)-?\d+(?:\.\d+)?(?!\S)'

def generator_numbers(text: str):
    numbers = re.findall(number_pattern, text)
    for number in numbers:
        yield float(number)

def sum_profit(text: str, func: Callable):
    return sum(func(text))
