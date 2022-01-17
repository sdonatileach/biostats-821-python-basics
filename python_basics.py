# # Python "data science"

# Develop two Python functions:

file = "/mnt/c/sdona/Documents/Duke/22Spring/821BIOSTAT/01Assignment/example.txt"
# ## `get_data()`
def get_data(file):

# _accepts_: a file path (string) and
    integers = []
    with open(file) as file:
        for line in file:
            l = line.split()
            integers.append(l)
        file.close()
    return integers
    


# _outputs_: a list of lists of integers.

# The file will contain two lines of integers separated by spaces, for example:
# ```text
# 1 44 31 4 5 6
# 21 3 2 13 55 72
# ```
def average(lst):
    return sum(lst)/len(lst)
# ## `analyze_data()`
def analyze_data(integers):
    new_list = integers[0] + integers[1]
    average(new_list)


# _accepts_:
# 1. a list of lists of integers and
# 2. a string option that can be one of the following:
#     * `"average"` (of all the data together)
#     * `"standard deviation"` (of all the data together)
#     * `"covariance"` (between the two lists)
#     * `"correlation"` ([Pearson's correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient))
# and

# _outputs_: a floating-point number.

# For the above example, your results should be about 21.4, 22.9, -257, and -0.594, respectively.

# ## constraints
# * You must submit your work in the form of a GitHub repository.
#   1. Invite the GitHub user `patrickkwang` to collaborate on your repository.
#   2. Include a link to the repository in the text of your Sakai submission.
# * You must work in group of 2 or 3 (not alone - we're practicing collaboration). We expect to see commits from each student, though you're welcome to pair-program as well.
# * You may `import math`, but no other packages, standard or otherwise.