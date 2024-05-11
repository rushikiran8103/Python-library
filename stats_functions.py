import math

# Function to calculate the mean of a list of numbers
def mean(numbers):
    if not numbers:
        raise ValueError("List of numbers cannot be empty")
    return sum(numbers) / len(numbers)

# Function to calculate the median of a list of numbers
def median(numbers):
    if not numbers:
        raise ValueError("List of numbers cannot be empty")
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        return sorted_numbers[n // 2]

# Function to calculate the variance of a list of numbers
def variance(numbers):
    if not numbers:
        raise ValueError("List of numbers cannot be empty")
    avg = mean(numbers)
    variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
    return variance

# Function to calculate the standard deviation of a list of numbers
def standard_deviation(numbers):
    return math.sqrt(variance(numbers))

# Function to calculate the correlation coefficient between two lists of numbers
def correlation_coefficient(x, y):
    if len(x) != len(y):
        raise ValueError("Lists must have the same length")
    n = len(x)
    mean_x = mean(x)
    mean_y = mean(y)
    covariance = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)) / n
    std_dev_x = standard_deviation(x)
    std_dev_y = standard_deviation(y)
    return covariance / (std_dev_x * std_dev_y)

# Function to calculate the covariance between two sets of numbers
def covariance(x, y):
    if len(x) != len(y):
        raise ValueError("Lists must have the same length")
    n = len(x)
    mean_x = mean(x)
    mean_y = mean(y)
    covariance = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)) / n
    return covariance

# Function to calculate percentage
def calculate_percentage(value, total):
    if total == 0:
        raise ValueError("Total value cannot be zero")
    percentage = (value / total) * 100
    return percentage

# Function to calculate the correlation matrix
def correlation_matrix(data):
    n = len(data)
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = correlation_coefficient(data[i], data[j])
    return matrix
