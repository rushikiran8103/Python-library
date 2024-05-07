def mean(numbers):
    if not numbers:
        raise ValueError("List of numbers cannot be empty")
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        raise ValueError("List of numbers cannot be empty")
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        return sorted_numbers[n // 2]

def variance(numbers):
    if not numbers:
        raise ValueError("List of numbers cannot be empty")
    avg = mean(numbers)
    variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
    return variance

def standard_deviation(numbers):
    return math.sqrt(variance(numbers))

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

