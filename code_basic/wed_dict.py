# ===================== 代码1：创建SEM图信息字典 =====================
# 键(key)：信息名称（如name, width）；值(value)：具体的信息内容
sem_info = {
    "name": "SEM-颗粒-01.jpg",
    "width": 1920,
    "scale": "100nm/像素",
    "particle_count": 25
}

# 打印整个字典，验证创建成功
print("=== 代码1：创建SEM图信息字典 ===")
print(f"SEM图完整信息：{sem_info}")
# 演示：通过键直接取值（精准获取颗粒数）
print(f"直接获取颗粒数：{sem_info['particle_count']} 个")

# ===================== 代码2：遍历字典打印所有键值对 =====================
print("\n=== 代码2：遍历字典（键值对） ===")
# .items() 会返回一个个(key, value)元组，循环中用两个变量接收
for key, value in sem_info.items():
    # 使用f-string格式化输出，让键占15个字符宽度，对齐更美观
    print(f"【{key:15}】-> {value}")

# ===================== 实操题（2道） =====================
print("\n=== 实操题解答 ===")

# 实操题1：修改与新增键值对
# 需求：1. 将图片宽度修改为 2048；2. 新增一个"height"键，值为1080
sem_info["width"] = 2048  # 直接通过键赋值，存在则修改
sem_info["height"] = 1080 # 直接通过键赋值，不存在则新增
print(f"1. 修改宽度并新增高度后：{sem_info}")

# 实操题2：安全获取不存在的键（避免KeyError报错）
# 需求：尝试获取"exposure_time"（曝光时间），若不存在则返回默认值"未记录"
# 方法：使用 .get(key, 默认值)，比直接用 [] 更安全，适合处理实验数据的缺失值
exposure = sem_info.get("exposure_time", "未记录")
print(f"2. 曝光时间：{exposure}")

# 拓展：如果后续测得了曝光时间，再添加进去
sem_info["exposure_time"] = "50ms"
exposure = sem_info.get("exposure_time", "未记录")
print(f"   补充曝光时间后： {exposure}")
