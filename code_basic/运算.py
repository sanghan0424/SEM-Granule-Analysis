# ===================== 代码1：根据SEM比例尺计算颗粒实际尺寸 =====================
# 1. 定义已知参数（贴合你的03.jpg/04.jpg场景）
pixel_diameter = 5 # 颗粒在SEM图中测量的像素直径
scale = 100        # 比例尺：1像素 = 100nm（03.jpg的基础比例尺）

# 2. 核心运算：像素尺寸 × 比例尺 = 实际尺寸（Python用*表示乘法）
actual_diameter_nm = pixel_diameter * scale

# 3. 打印结果（清晰标注单位，便于实验记录）
print("=== 代码1：SEM颗粒实际尺寸计算 ===")
print(f"颗粒像素直径：{pixel_diameter} 像素")
print(f"SEM图比例尺：1像素 = {scale} nm")
print(f"颗粒实际直径：{actual_diameter_nm} nm")

# 拓展：转换为μm（1μm = 1000nm，用/表示除法）
actual_diameter_um = actual_diameter_nm / 1000
print(f"颗粒实际直径（μm）：{actual_diameter_um} μm")

# ===================== 实操题（2道） =====================
print("\n=== 实操题解答 ===")

# 实操题1：适配04.jpg的大比例尺换算（300μm/像素）
# 需求：04.jpg中某颗粒像素直径为8像素，比例尺1像素=300μm，计算实际尺寸（转mm）
pixel_dia_04 = 8
scale_04 = 300
actual_dia_um = pixel_dia_04 * scale_04
actual_dia_mm = actual_dia_um /1000
print(f"1. 04.jpg颗粒计算：")
print(f"   像素直径：{pixel_dia_04} 像素 -> 实际直径：{actual_dia_um} μm = {actual_dia_mm} mm ")

# 实操题2：多颗粒平均尺寸计算（混合+/*运算）
# 需求：测量3颗颗粒的像素直径（4、6、5），比例尺100nm/像素，计算平均实际尺寸
pixel_list = [4, 6, 5] #3颗颗粒的像素直径
total_pixel = sum(pixel_list) #求和 (+运算)
avg_pixel = total_pixel / len(pixel_list) #求平均（/运算）
avg_actual_nm = avg_pixel * 100 # 换算实际尺寸（*运算）
print(f"2. 多颗粒平均尺寸计算：")
print(f"   3颗颗粒像素直径：{pixel_list}")
print(f"   平均像素直径：{avg_pixel} 像素 → 平均实际尺寸：{avg_actual_nm} nm")
