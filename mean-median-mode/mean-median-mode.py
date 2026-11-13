from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # 1. Tính Mean (Trung bình cộng) bằng NumPy và ép về float
    mean_val = float(np.mean(x))
    
    # 2. Tính Median (Trung vị) bằng NumPy và ép về float
    median_val = float(np.median(x))
    
    # 3. Tính Mode (Yếu vị - giá trị xuất hiện nhiều nhất)
    counts = Counter(x)
    max_freq = max(counts.values())
    # Lọc tất cả các số có tần suất bằng max_freq và lấy số nhỏ nhất (min)
    mode_val = float(min(k for k, v in counts.items() if v == max_freq))
    
    return {
        "mean": mean_val,
        "median": median_val,
        "mode": mode_val
    }