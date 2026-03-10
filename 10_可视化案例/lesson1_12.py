"""
# 数据可视化-动态柱状图
# 通过pyecharts可以实现数据的动态显示，直观的感受1960~2019年全世界各国GDP的变化趋势

# 基础柱状图
# 通过Bar构建基础柱状图
from pyecharts.charts import Bar
from pyecharts.options import *

# 构建柱状图对象
bar=Bar()
# 添加x轴数据
bar.add_xaxis(["中国","美国","英国"])
# 添加y轴数据
bar.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="top"))
# 绘图
bar.render("GDP柱状图.html")

# 反转x和y轴
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

# 构建柱状图对象
bar=Bar()
# 添加x轴数据
bar.add_xaxis(["中国","美国","英国"])
# 添加y轴数据
bar.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="right"))
# 反转xy轴
bar.reversal_axis()
# 绘图
bar.render("基础柱状xy反转图.html")

# 时间线配置动态图表

# 创建时间线
# Timeline()---时间线
# 柱状图描述的是分类数据，回答的是每一个分类中『有多少？』这个问题.
# 这是柱状图的主要特点,同时柱状图很难动态的描述一个趋势性的数据.
# 这里pyecharts为我们提供了一种解决方案-时间线
# 如果说一个Bar、Line对象是一张图表的话，时间线就是创建一个一维的x轴，轴上每一个点就是一个图表对象

# 创建时间线
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *

bar1 = Bar()
bar1.add_xaxis(["中国","美国","英国"])
bar1.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国","美国","英国"])
bar2.add_yaxis("GDP",[50,30,20],label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国","美国","英国"])
bar3.add_yaxis("GDP",[80,70,30],label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

#创建时间线对象
# 时间线设置主题
from pyecharts.globals import ThemeType
timeline=Timeline(
    {"theme":ThemeType.LIGHT}
)
#timeLine对象添加bar柱状图
timeline.add(bar1, "2021年GDP")
timeline.add(bar2,"2022年GDP")
timeline.add(bar3,"2023年GDP")

# 自动播放设置
timeline.add_schema(
    play_interval=1000,      # 自动播放的时间间隔，单位毫秒
    is_timeline_show=True,   # 是否在自动播放的时候，显示时间线
    is_auto_play=True,       # 是否自动播放
    is_loop_play=True        # 是否循环播放
)
#通过时间线绘图
# 绘图是用时间线对象绘图，而不是bar对象了
timeline.render("基础柱状图-时间线.htmL")


# 扩展列表的sort方法
# 在学习了将函数作为参数传递后，我们可以学习列表的sort方法来对列表进行自定义排序

# 列表的sort方法:
# 使用方式：
# 列表.sort(key=选择排序依据的函数, reverse=True|False)
# 参数key，是要求传入一个函数，表示将列表的每一个元素都传入函数中，返回排序的依据
# 参数reverse，是否反转排序结果，True表示降序，False表示升序


# 准备列表
my_list = [["a", 33], ["b", 55], ["c", 11]]

# 排序，基于带名函数
# def choose_sort_key(element):
#     return element[1]
# my_list.sort(key=choose_sort_key, reverse=True)

# 排序，基于lambda匿名函数
my_list.sort(key=lambda element: element[1], reverse=True)
print(my_list)
"""

# 演示第三个图表：GDP动态柱状图开发
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

# 读取数据
f = open("D:/个人/learning/python/可视化案例数据/动态柱状图数据/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
data_lines = f.readlines()
# 关闭文件
f.close()
# 删除第一条数据
data_lines.pop(0)
# 将数据转换为字典存储，格式为：
# { 年份: [ [国家, gdp], [国家,gdp], ......  ], 年份: [ [国家, gdp], [国家,gdp], ......  ], ...... }
# { 1960: [ [美国, 123], [中国,321], ......  ], 1961: [ [美国, 123], [中国,321], ......  ], ...... }
# 先定义一个字典对象
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])      # 年份
    country = line.split(",")[1]        # 国家
    gdp = float(line.split(",")[2])     # gdp数据
    # 如何判断字典里面有没有指定的key呢？
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

# print(data_dict[1960])
# 创建时间线对象
timeline = Timeline({"theme": ThemeType.LIGHT})
# 排序年份
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 取出本年份前8名的国家
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])   # x轴添加国家
        y_data.append(country_gdp[1] / 100000000)   # y轴添加gdp数据

    # 构建柱状图
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    # 反转x轴和y轴
    bar.reversal_axis()
    # 设置每一年的图表的标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8GDP数据")
    )
    timeline.add(bar, str(year))


# for循环每一年的数据，基于每一年的数据，创建每一年的bar对象
# 在for中，将每一年的bar对象添加到时间线中

# 设置时间线自动播放
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)
# 绘图
timeline.render("1960-2019全球GDP前8国家.html")
