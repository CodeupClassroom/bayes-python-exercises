import numpy as np

numbers = [1, 2, 3, 4, 5, 6]

a = np.array(numbers)

# Exercises
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# How many negative numbers are there?
negatives = a[a < 0]
len(negatives)

# How many positive numbers are there?
positives = a[a > 0]
len(positives)

# How many positive evens
positive_evens = positives[positives % 2 == 0]
len(positive_evens)

# Add 3 to each data point
a + 3

# Once squared, what is the new mean and standard deviation
squares = a**2
squares.mean()
squares.std()

# "Centering" the dataset means  to adjust the data so that the center of the data is at 0. 
# To center, subtract the eman from each data point
mean = a.mean()
centered = a - mean
centered

# Calculate the z-score for each data point. Recall that the z-score is given by:
# Z = (x - µ) / σ
z_scores = (a - a.mean()) / a.std()
z_scores

# Below are exercises from https://gist.github.com/ryanorsinger/c4cf5a64ec33c014ff2e56951bc8a42d

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.