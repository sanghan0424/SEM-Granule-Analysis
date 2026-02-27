"""
颗粒粒径有效性判断脚本
适配场景：SEM图像颗粒分析，判断粒径是否符合业务规则（0.5μm≤粒径≤5μm）
作者：实习开发者
创建时间：2026-02-27
"""
from sympy.codegen.fnodes import elemental

# 模拟从SEM图像中提取的颗粒粒径数据（单位：μm）
granule_sizes = [0.2, 1.3, 5.8, 3.1, 0.9]

# 打印业务规则提示（提升可读性）
print("===== 颗粒粒径有效性判断（业务规则：0.5μm≤粒径≤5μm）=====\n")

# 遍历所有粒径，逐行判断
for size in granule_sizes:
 #严格按业务规则判断
    if size <0.5:
        print(f"粒径{size}μm：无效（过小，低于0.5μm阈值）")
    elif size > 5:
        print(f"粒径{size}μm：无效（过大，高于5μm阈值）")
    else:
        print(f"粒径{size}μm：有效，计入统计")

# 拓展：统计有效/无效颗粒数量（可选，提升代码实用性）
valid_count = 0    # 有效颗粒数
invalid_count = 0  # 无效颗粒数
for size in granule_sizes:
    if 0.5 <= size <= 5:
        valid_count += 1
    else:
        invalid_count += 1

# 打印统计结果
print(f"\n===== 统计结果 =====")
print(f"有效颗粒数：{valid_count} 个")
print(f"无效颗粒数：{invalid_count} 个")
print(f"有效率：{valid_count / len(granule_sizes) * 100:.1f} % ")




