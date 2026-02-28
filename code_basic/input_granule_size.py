"""
颗粒粒径手动输入判断脚本
功能：循环接收粒径输入，判断有效性，输入q退出
适配场景：SEM颗粒粒径手动录入、实时判断
作者：实习开发者
创建时间：2026-02-28
"""

# 定义有效阈值（复用项目统一标准）
MAX_VALID_SIZE = 5.0  # 最大有效粒径（μm）
MIN_VALID_SIZE = 0.5  # 最小有效粒径（μm）

print("===== 颗粒粒径有效性判断程序 =====")
print(f"有效粒径范围：{MIN_VALID_SIZE} ~ {MAX_VALID_SIZE} μm , 输入q退出程序")

# 核心：while无限循环，直到输入q退出
while True:
    #接受用户输入
    size_input = input("请输入颗粒粒径（μm）：")

    # 1. 判断是否退出
    if size_input.strip().lower() == "q":  # 兼容大小写、空格
        print("\n✅ 程序正常退出，感谢使用！")
        break  # 终止循环
    # 2. 异常处理： 非数字输入
    try:
        # 转换为浮点数（兼容整数/小数输入）
        granule_size = float(size_input)

        # 3. 判断粒径有效性
        if granule_size < 0:
            print(f"❌ 输入错误：粒径{granule_size}μm为负数，无物理意义！")
            continue  # 跳过后续，直接进入下一次循环
        elif MIN_VALID_SIZE <= granule_size <= MAX_VALID_SIZE:
            print(f"✅ 粒径{granule_size}μm：有效颗粒（符合{MIN_VALID_SIZE}~{MAX_VALID_SIZE}μm阈值）")
        else:
            print(f"❌ 粒径{granule_size}μm：无效颗粒（超出{MIN_VALID_SIZE}~{MAX_VALID_SIZE}μm阈值）")

    # 捕获所有非数字输入的异常
    except ValueError:
        print(f"❌ 输入错误：'{size_input}'不是有效数字，请输入数字或q退出！")

# 程序结束（循环终止后执行）
print("\n📊 本次输入结束，可查看judge_granule.py获取批量统计结果")