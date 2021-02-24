import re, numpy
import matplotlib.pyplot as plt
import pylab as pl

# 创建空列表
ticket = []
# 打开存储数据的文件
f = open('tieba.txt',  encoding='utf-8')
# 逐行读取文件
lines = f.readlines()
# 因为读取出来的文件是str，所以要从新提取出票，重新存入list
for line in lines:
    result = re.findall('\d*号候选人', line)
    ticket += result


# 这一段代码的目的为统计列表中每个元素出现的次数，并保存为字典，即K为候选人，V为票数
arr = numpy.array(ticket)
key = numpy.unique(ticket)
statistics = {}
for k in key:
    mask = (arr == k)
    arr_new = arr[mask]
    v = arr_new.size
    statistics[k] = v

# 将上面统计出来的dic绘制成直方图，可以直观的看到数据
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.figure(figsize=(38.40, 21.60), dpi=100)
plt.title("B吧大选")
x = range(len(statistics))
x_ticks = list(statistics.keys())
plt.xticks(x[::1], x_ticks[::1])
pl.xticks(rotation=270) # x轴标签翻转270度
y_ticks = list(statistics.values())
y = y_ticks
plt.bar(x, y)
plt.savefig("tieba.png")