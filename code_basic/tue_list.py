# ===================== 代码1：创建列表存储SEM图颗粒数量 =====================
# 列表名：particle_count，存储4张SEM图（01/02/03/04.jpg）的颗粒数量
particle_count = [25, 32, 28, 30]
# 打印原始列表，验证创建成功
print("=== 代码1：SEM图颗粒数量列表 ===")
print(f"4张SEM图的颗粒数量：{particle_count}")

# ===================== 代码2：计算列表平均值 =====================
# sum(particle_count)：求和；len(particle_count)：求元素个数；/ 除法计算平均值
avg_count = sum(particle_count) / len(particle_count)
print("=== 代码2：计算平均值 ===")
print(f"颗粒数量总和：{sum(particle_count)}")
print(f"列表元素个数：{len(particle_count)}")
print(f"颗粒数量平均值：{avg_count:.2f}")

# ===================== 代码3：打印列表最大值/最小值 =====================
max_count = max(particle_count) #最大值
min_count = min(particle_count)
print("=== 代码3：最大值/最小值 ===")
print(f"最多颗粒数：{max_count}")
print(f"最少颗粒数：{min_count}")

# ===================== 实操题（3道） =====================
print("\n=== 实操题解答 ===")
# 实操题1：给列表新增第5张SEM图的颗粒数（35），并重新计算平均值
particle_count.append(35)  #append()向列表末尾添加元素
new_avg = sum(particle_count) / len(particle_count)
print(f"1. 新增颗粒数35后，列表：{particle_count}, 新品均值：{new_avg:.2f}")

# 实操题2：修改第2张图的颗粒数（32→34），并打印修改后的列表
particle_count[1] = 34
print(f"2. 修改第2张图颗粒数后，列表：{particle_count}")

# 实操题3：删除列表中最小值（25），并打印删除后的列表
particle_count.remove(min(particle_count))   # remove() 删除指定元素
print(f"3. 删除最小值后，列表：{particle_count}")





