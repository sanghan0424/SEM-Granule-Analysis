# ===================== 代码1：存储SEM图像尺寸 =====================
# 定义变量存储SEM图像的宽度和高度（单位：像素）
sem_img_width = 1920   # 图像宽度
sem_img_height = 1080  # 图像高度
# 可选：定义图像分辨率（像素/英寸）
sem_img_dpi = 300

# ===================== 代码2：存储SEM拍摄参数 =====================
# 定义变量存储SEM拍摄的关键参数
sem_voltage = 15       # 加速电压，单位：kV
sem_work_distance = 8  # 工作距离，单位：mm
sem_magnification = 5000  # 放大倍数（补充常用参数）
sem_detector = "SE"    # 探测器类型（SE=二次电子，BSE=背散射电子）

# ===================== 代码3：打印验证变量（可选） =====================
# 打印图像尺寸参数
print("=== SEM图像尺寸参数 ===")
print(f"图像宽度：{sem_img_width} 像素")
print(f"图像高度：{sem_img_height} 像素")
print(f"图像分辨率：{sem_img_dpi} DPI")

# 打印拍摄参数
print("\n=== SEM拍摄参数 ===")
print(f"加速电压：{sem_voltage} kV")
print(f"工作距离：{sem_work_distance} mm")
print(f"放大倍数：{sem_magnification} 倍")
print(f"探测器类型：{sem_detector}（二次电子）")