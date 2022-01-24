"""BIOSTATS Assignment 1 Mohammad Anas, Aarushi Verma, Sydney Donati-Leach."""

import math
from typing import TextIO, Union

file = "/Users/Aarushi/Duke/MIDS/Spring 2022/821_BIOSTAT/HW/python-basics-biostats-821/example.txt"


def get_data(file: TextIO) -> list[list[int]]:
    """Return data as a list of lists of integers."""
    integers = []  # list of list of integers
    with open(file) as file:

        for line in file:
            lst_int = line.split()  # go over each line and create a list of string
            lst_int = [int(i) for i in lst_int]  # convert strings to integers
            integers.append(lst_int)  # append the list to integers list
        file.close()

    return integers


def average(lst: list[int]) -> float:
    """Compute the average of a list."""
    return sum(lst) / len(lst)


def standard_dev(lst: list[int]) -> float:
    """Compute the standard deviation of a list."""
    avg = average(lst)
    sum = 0
    for i in lst:
        sum += (i - avg) ** 2  # we subtract each value from average and square it
    var = sum / len(lst)  # defining variance
    return math.sqrt(var)  # returns standard deviation


def cov(lst1: list[int], lst2: list[int]) -> float:
    """Compute covariance of two lists."""
    avg_1 = average(lst1)
    avg_2 = average(lst2)
    sum = 0
    for i in range(len(lst1)):
        sum += (lst1[i] - avg_1) * (
            lst2[i] - avg_2
        )  # we loop over both the lists and perform required calculations on each element
    cov = sum / len(lst1)  # and then add the value to the sum variable defined
    return cov


def corr(lst1: list[int], lst2: list[int]) -> float:
    """Compute correlation of two lists."""
    cov_ = cov(lst1, lst2)
    std1 = standard_dev(lst1)
    std2 = standard_dev(lst2)
    std_ = std1 * std2

    return cov_ / std_


def analyze_data(
    integers: list[list[int]], operation: str = "average"
) -> Union[str, float]:
    """Perform the stated operation on the data."""
    """The default operation has been set to the average."""
    new_list = (
        integers[0] + integers[1]
    )  # combine two lists for mean and std dev functions

    lst1 = integers[0]
    lst2 = integers[1]

    # conditional statements to perform operations
    if operation == "average":
        ans = round(average(new_list), 2)
        return ans

    elif operation == "standard deviation":
        ans = round(standard_dev(new_list), 2)
        return ans

    elif operation == "covariance":
        ans = round(cov(lst1, lst2), 2)
        return ans

    elif operation == "correlation":
        ans = round(corr(lst1, lst2), 2)
        return ans

    else:
        return "Enter the right operation value"  # we handle exceptions in regards to the operations performed here
