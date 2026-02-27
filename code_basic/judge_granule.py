"""
颗粒粒径有效性判断脚本（优化版）
新增：for循环统计有效颗粒数+占比，适配多批次颗粒分析
适配场景：SEM多晶粒颗粒粒径统计
作者：实习开发者
创建时间：2026-02-28
"""

# 模拟从SEM多晶粒图像中提取的颗粒粒径数据（单位：μm）
granule_sizes = [0.2, 1.3, 5.8, 3.1, 0.9, 4.5, 6.2, 0.4, 2.7, 5.0]

# 1. 基础判断：遍历每个粒径，输出有效性
print("===== 颗粒粒径有效性判断（业务规则：0.5μm≤粒径≤5μm）=====\n")
for size in granule_sizes:
    if size < 0.5:
        print(f"粒径{size}μm：无效（过小，低于0.5μm阈值）")
    elif size > 5:
        print(f"粒径{size}μm：无效（过大，高于5μm阈值）")
    else:
        print(f"粒径{size}μm：有效，计入统计")

# 2. 核心优化：for循环统计有效颗粒数+占比
valid_count = 0  # 初始化有效颗粒计数器
# 遍历粒径列表，统计有效数量
for size in granule_sizes:
    if 0.5 <= size <= 5:
        valid_count += 1  # 符合条件则计数器+1

# 计算占比（保留1位小数）
total_count = len(granule_sizes)
valid_ratio = valid_count / total_count * 100

# 输出统计结果（贴合科研报告格式）
print(f"\n===== 统计结果 ======")
print(f"总颗粒数：{total_count} 个")
print(f"有效颗粒数：{valid_count} 个")
print(f"有效颗粒占比：{valid_ratio:.1f}%")

# 3. 拓展：for循环生成批次报告（可选，加深理解）
batch_names = ["批次1（晶粒取向1）", "批次2（晶粒取向2）"]
for batch in batch_names:
    print(f"\n【{batch}】有效颗粒占比参考值：{valid_ratio:.1f}%")