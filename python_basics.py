# BIOSTATS Assignment 1
# Mohammad Anas, Aarushi Verma, Sydney Donati-Leach

import math

file = "/Users/mohammadanas/Desktop/Duke MIDS/Spring 2021/SoftwareTools/Assignment_1/python-basics-biostats-821/example.txt"


def get_data(file: str) -> list[list[int]]:
    """This function return the data as a list of lists"""
    integers = []
    with open(file) as file:
        for line in file:
            l = line.split()
            integers.append(l)
        file.close()
    lst1 = [int(i) for i in integers[0]]
    lst2 = [int(i) for i in integers[1]]
    return lst1 + lst2


def average(lst: list[int]) -> int:
    return sum(lst) / len(lst)


def standard_dev(lst: list[int]) -> int:
    avg = average(lst)
    integer = 0
    for i in lst:
        integer += (i - avg) ** 2
    a = integer / len(lst)
    return math.sqrt(a)


def cov(lst1, lst2) -> int:
    avg_1 = average(lst1)
    avg_2 = average(lst2)
    sum = 0
    for i in range(len(lst1)):
        sum += (lst1[i] - avg_1) * (lst2[i] - avg_2)
    cov = sum / len(lst1)
    return cov


def corr(lst1, lst2) -> int:

    cov_ = cov(lst1, lst2)
    std1 = standard_dev(lst1)
    std2 = standard_dev(lst2)
    std_ = std1 * std2

    return cov_ / std_


def analyze_data(integers, operation="average")  -> int:
    """This function perform the stated operation on the data.
    The default operation has been set to the average"""

    new_list = integers[0] + integers[1]

    one_list = [int(i) for i in new_list]
    lst1 = [int(i) for i in integers[0]]
    lst2 = [int(i) for i in integers[1]]

    if operation == "average":
        ans = round(average(one_list), 2)
        print("The average is", ans)

    elif operation == "standard deviation":
        ans = round(standard_dev(one_list), 2)
        print("The standard deviation is", ans)

    elif operation == "covariance":
        ans = round(cov(lst1, lst2), 2)
        print("The covariance is", ans)

    elif operation == "correlation":
        ans = round(corr(lst1, lst2), 2)
        print("The correlation is", ans)

    else:
        return "Enter the right operation value"
