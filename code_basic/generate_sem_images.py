import numpy as np
import cv2  # 需要安装opencv-python，若未安装先执行：pip install opencv-python

# 定义项目路径（适配你的D盘目录）
project_path = r"D:\SEM-Granule-Analysis"
raw_data_path = f"{project_path}/data_raw_sem"


# 1. 创建模拟SEM图的核心函数
def generate_sem_granule_image(is_thick: bool, save_path: str):
    """
    生成模拟SEM颗粒图：厚颗粒（亮）/薄颗粒（暗）
    :param is_thick: True=厚颗粒（亮），False=薄颗粒（暗）
    :param save_path: 图片保存路径
    """
    # 设置图片尺寸（500x500，模拟SEM图像分辨率）
    img_size = (500, 500)
    # 创建背景（灰度图，0=黑，255=白）
    if is_thick:
        # 厚颗粒：背景亮（180）+ 颗粒更亮（220-255）
        background = np.ones(img_size, dtype=np.uint8) * 180
        granule_intensity = (220, 255)
    else:
        # 薄颗粒：背景暗（80）+ 颗粒稍暗（100-130）
        background = np.ones(img_size, dtype=np.uint8) * 80
        granule_intensity = (100, 130)

    # 生成随机颗粒（模拟SEM中的颗粒分布）
    np.random.seed(42)  # 固定随机种子，保证每次生成的颗粒位置一致
    num_granules = 50  # 颗粒数量
    for _ in range(num_granules):
        # 随机生成颗粒中心坐标和半径
        x = np.random.randint(50, img_size[0] - 50)
        y = np.random.randint(50, img_size[1] - 50)
        radius = np.random.randint(10, 30) if is_thick else np.random.randint(5, 20)

        # 绘制圆形颗粒（模拟SEM中的颗粒）
        cv2.circle(
            background,
            (x, y),
            radius,
            np.random.randint(*granule_intensity),  # 颗粒亮度
            -1  # 填充圆形
        )

    # 添加噪声（模拟SEM图像的电子噪声）
    noise = np.random.normal(0, 5, img_size).astype(np.uint8)
    img = cv2.add(background, noise)

    # 保存图片
    cv2.imwrite(save_path, img)
    print(f"✅ 模拟SEM图已生成：{save_path}")


# 2. 生成厚/亮颗粒图
thick_img_path = f"{raw_data_path}/thick_granule.jpg"
generate_sem_granule_image(is_thick=True, save_path=thick_img_path)

# 3. 生成薄/暗颗粒图
thin_img_path = f"{raw_data_path}/thin_granule.jpg"
generate_sem_granule_image(is_thick=False, save_path=thin_img_path)

# 4. 验证文件是否生成
import os

if os.path.exists(thick_img_path) and os.path.exists(thin_img_path):
    print("\n🎉 所有模拟SEM图生成完成！文件位置：")
    print(f"- 厚/亮颗粒：{thick_img_path}")
    print(f"- 薄/暗颗粒：{thin_img_path}")
else:
    print("\n❌ 图片生成失败，请检查路径是否正确！")