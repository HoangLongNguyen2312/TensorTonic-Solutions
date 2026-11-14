import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    arr = np.asarray(x, dtype=float)
    n = arr.size
    
    # Bước 1: Tính trung bình mẫu (x_bar) và độ lệch từng phần tử (xi - x_bar)
    centered = arr - np.mean(arr)
    
    # Bước 2: Tính tổng bình phương độ lệch rồi chia cho (n - 1)
    variance = np.sum(centered ** 2) / (n - 1)
    
    # Bước 3: Lấy căn bậc hai để ra độ lệch chuẩn mẫu
    std_dev = np.sqrt(variance)
    
    # Bước 4: Ép kiểu về float chuẩn của Python và trả về đúng key yêu cầu
    return {
        "variance": float(variance),
        "standard_deviation": float(std_dev)
    }