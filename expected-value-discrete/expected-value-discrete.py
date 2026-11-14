import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Chuyển đầu vào thành mảng NumPy kiểu float để tính toán
    x_arr = np.asarray(x, dtype=float)
    p_arr = np.asarray(p, dtype=float)
    
    # Kiểm tra điều kiện hợp lệ (kích thước khớp nhau & tổng xác suất bằng 1)
    if x_arr.shape != p_arr.shape:
        raise ValueError("x and p must have the same shape")
    if not np.isclose(np.sum(p_arr), 1.0):
        raise ValueError("Probabilities must sum to 1")
        
    # Tính tổng tích vô hướng sum(x_i * p_i) và ép về kiểu float của Python
    ev = np.sum(x_arr * p_arr)
    return float(ev)