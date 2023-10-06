# grade_calculator.py

def calculate_mean(scores):
    """
    Calculate the mean (average) of a list of scores.

    Args:
        scores (list): List of student scores.

    Returns:
        float: The mean of the scores.
    """
    if not scores:
        return 0  # Return 0 for an empty list to avoid division by zero.
    
    total_score = sum(scores)
    mean = total_score / len(scores)
    return mean

def calculate_median(scores):
    """
    Calculate the median of a list of scores.

    Args:
        scores (list): List of student scores.

    Returns:
        float: The median of the scores.
    """
    sorted_scores = sorted(scores)
    n = len(sorted_scores)
    if n % 2 == 0:
        # If the number of scores is even, take the average of the middle two scores.
        middle1 = sorted_scores[n // 2 - 1]
        middle2 = sorted_scores[n // 2]
        median = (middle1 + middle2) / 2
    else:
        # If the number of scores is odd, take the middle score.
        median = sorted_scores[n // 2]
    
    return median
