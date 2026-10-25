import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.

    Args:
        data: List or numpy array of numerical values

    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    if len(data) == 0:
        raise ValueError("Dataset cannot be empty.")

    data = np.array(data)

    # Mean and Median
    mean = np.mean(data)
    median = np.median(data)

    # Mode
    unique_values, counts = np.unique(data, return_counts=True)
    mode = unique_values[np.argmax(counts)]

    # Variance and Standard Deviation
    variance = np.var(data)
    std_dev = np.std(data)

    # Percentiles
    p25 = np.percentile(data, 25)
    p50 = np.percentile(data, 50)
    p75 = np.percentile(data, 75)

    # Interquartile Range
    iqr = p75 - p25

    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": variance,
        "standard_deviation": std_dev,
        "25th_percentile": p25,
        "50th_percentile": p50,
        "75th_percentile": p75,
        "interquartile_range": iqr,
    }