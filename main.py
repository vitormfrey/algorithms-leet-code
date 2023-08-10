# This is a sample Python script.
from typing import List

from binary_search import SolutionBinarySearch
from two_sum import SolutionTwoSum
from valid_anagram import SolutionAnagram


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


s = SolutionBinarySearch()
s.binarySearch([1,2,3,4,5,6,7,8,9,10, 11], 11)