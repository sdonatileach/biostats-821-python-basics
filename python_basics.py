"""BIOSTATS Assignment 1 Mohammad Anas, Aarushi Verma, Sydney Donati-Leach """

import math

file = "/Users/mohammadanas/Desktop/Duke MIDS/Spring 2021/SoftwareTools/Assignment_1/python-basics-biostats-821/example.txt"


def get_data(file: str) -> list[list[int]]:
    """This function return the data as a list of lists of integer"""
    integers = []  # list of list of integers
    with open(file) as file:  # open the file
        for line in file:
            lst_int = line.split()  # go over each line and create a list of string
            lst_int = [int(i) for i in lst_int]  # convert strings to integers
            integers.append(l)  # append the list to integers list
        file.close()

    return integers


def average(lst: list[int]) -> int:
    """Compute the average of a list"""
    return sum(lst) / len(lst)


def standard_dev(lst: list[int]) -> int:
    """Computes the standard deviation of a list"""
    avg = average(lst)
    sum = 0
    for i in lst:
        sum += (i - avg) ** 2  # we subtract each value from average and square it
    var = sum / len(lst)  # defining variance
    return math.sqrt(var)  # returns standard deviation


def cov(lst1, lst2) -> int:
    """This function computes covariance of two lists"""
    avg_1 = average(lst1)
    avg_2 = average(lst2)
    sum = 0
    for i in range(len(lst1)):
        sum += (lst1[i] - avg_1) * (
            lst2[i] - avg_2
        )  # we loop over both the lists and perform required calculations on each element
    cov = sum / len(lst1)  # and then add the value to the sum variable defined
    return cov


def corr(lst1, lst2) -> int:
    """This function computes correlation of two lists"""
    cov_ = cov(lst1, lst2)
    std1 = standard_dev(lst1)
    std2 = standard_dev(lst2)
    std_ = std1 * std2

    return cov_ / std_


def analyze_data(integers, operation="average") -> int:
    """This function perform the stated operation on the data.
    The default operation has been set to the average"""

    new_list = (
        integers[0] + integers[1]
    )  # we combine the two lists in our data for mean and standard deviations functions

    lst1 = integers[0]
    lst2 = integers[1]

    if operation == "average":
        ans = round(average(new_list), 2)
        print(
            "The average is", ans
        )  # use conditional statements to to perform the required operations

    elif operation == "standard deviation":
        ans = round(standard_dev(new_list), 2)
        print("The standard deviation is", ans)

    elif operation == "covariance":
        ans = round(cov(lst1, lst2), 2)
        print("The covariance is", ans)

    elif operation == "correlation":
        ans = round(corr(lst1, lst2), 2)
        print("The correlation is", ans)

    else:
        return "Enter the right operation value"  # we handle exceptions in regards to the operations performed here
