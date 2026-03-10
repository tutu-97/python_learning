
# python基础综合案例  数据可视化-折线图可视化
# 效果一：2020年印美日新冠累计确诊人数
# 效果二：全国疫情地图可视化
# 效果三：动态GDP增长图

# 数据来源：本案例数据全部来自《百度疫情实时大数据报告》，及公开的全球各国GDP数据
# 使用的技术 Echarts是个由百度开源的数据可视化，凭借良好的交互性，精巧的图表设计，得到了众多开发者的认可
# 而Python 是门富有表达力的语言，很适合用于数据处理，当数据分析遇上数据可视化时pyecharts诞生了

# json数据格式
# json是一种轻量级的数据交互格式。可以按照JSON指定的格式去组织和封装数据JSON，本质上是一个带有特定格式的字符串
# 主要功能:json就是一种在各个编程语言中流通的数据格式，负责不同编程语言中的数据传递和交互类似于:
# 国际通用语言-英语
# 中国56个民族不同地区的通用语言-普通话
# 各种编程语言存储数据的容器不尽相同,在Python中有字典dict这样的数据类型，而其它语言可能没有对应的字典。
# 为了让不同的语言都能够相互通用的互相传递数据，JSON就是一种非常良好的中转数据格式。如下，以Python和C语言互传数据为例:
# python格式数据->json格式数据->C语言程序接受json格式数据并转化为C格式数据继续使用
# C格式数据->json格式数据->Python语言程序接受json格式数据并转化为Python格式数据继续使用

# json格式数据转化
# json格式的数据要求严格，要求：
# json数据的格式可以是：
var1 = {"name": "admin", "age": 18}
# json数据格式也可以是：
var2 = [{"name": "admin", "age": 18}, {"name": "root", "age": 16},{"name": "张三", "age": 20}]

# python数据和json数据的相互转化
# 导入json模块
import json

# 准备列表，列表内每一个元素都是字典，将其转换为json
data=[{"name":"老王","age":16},{"name":"张三","age":20}]
# 通过json.dumps()方法将python数据转化为json数据
json_str = json.dumps(data,ensure_ascii=False)
print(type(json_str))
print(json_str)

# 准备字典，将字典转换为json
d={"name":"老王","age":16}
# 通过json.dumps()方法将python数据转化为json数据
json_str = json.dumps(d,ensure_ascii=False)
print(type(json_str))
print(json_str)


# 通过json.loads()方法将json数据转化为python数据类型[{k:v,k:v},{k:v,k:v}]
s='[{"name":"老王","age":16},{"name":"张三","age":20},{"name":"李四","age":21}]'
l=json.loads(s)
print(type(l))
print(l)

# 通过json.loads()方法将json数据转化为python数据类型{k:v,k:v}
s='{"name":"老王","age":16}'
d=json.loads(s)
print(type(d))
print(d)


# pyecharts模块：想要做出数据可视化效果图，可以借助pyecharts模块来完成
# 概况：Echarts是一个是个由百度开源的数据可视化，凭借良好的交互性，精巧的图表设计，得到了众多开发者的认可
# 而Python 是门富有表达力的语言，很适合用于数据处理，当数据分析遇上数据可视化时pyecharts诞生了

# 官方网站：pyecharts.org
# 画廊：https://gallery.pyecharts.org/  可参考里面的案例代码，更改数据

# pyecharts模块安装
# 使用在前面学过的pip命令即可快速安装pyecharts模块

# pyecharts入门
# 基础折线图
# 导包,导入Line功能构建折线图对象
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts,TooltipOpts

# 得到折线图对象  空的坐标系
line=Line()
# 添加x轴数据
line.add_xaxis(["中国","美国","英国"])
# 添加y轴数据
line.add_yaxis("GDP",[30,20,10])

# pyecharts有哪些配置选项
# 常用2个类别的选项
# 全局配置选项: 配置图表的标题,配置图例,配置鼠标移动效果,配置工具栏等整体配置项
# 系列配置选项

# set_global_opts方法
# 这里全局配置选项可以通过set_global_opts方法来进行配置,相应的选项的功能如下:
# TitleOpts 标题配置项
# LegendOpts 图例配置项
# ToolboxOpts 工具箱配置项
# VisualMapOpts 视觉映射配置项
# TooltipOpts 提示框配置项

# 设置全局配置项set_global_opts来设置  关键字传参  control+p展示需要传的参数
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center",pos_bottom="1%"),
    legend_opts=LegendOpts(is_show= True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
    tooltip_opts=TooltipOpts(is_show=True)
)
# 生成图表
line.render()

# 数据处理 通过json模块对数据进行处理
# 懒人工具 ab173->json相关->json视图  理清层次结构
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LabelOpts

# 处理数据
f_us=open("D:\个人\\learning\\python\可视化案例数据\折线图数据\美国.txt","r",encoding="UTF-8")
us_data=f_us.read()   #美国的全部内容
f_jp=open("D:\个人\\learning\\python\可视化案例数据\折线图数据\日本.txt","r",encoding="UTF-8")
jp_data=f_jp.read()   #日本的全部内容
f_in=open("D:\个人\\learning\\python\可视化案例数据\折线图数据\印度.txt","r",encoding="UTF-8")
in_data=f_in.read()   #印度的全部内容
# 去掉不合json规范的开头
us_data=us_data.replace("jsonp_1629344292311_69436(","")
jp_data=jp_data.replace("jsonp_1629350871167_29498(","")
in_data=in_data.replace("jsonp_1629350745930_63180(","")
# 去除不合Json规范的结尾
# us_data.replace(");","")  错误，因为有可能替换多了 ); 出现数据错误
us_data=us_data[:-2]
jp_data=jp_data[:-2]
in_data=in_data[:-2]
# json转python字典
us_dict=json.loads(us_data)
jp_dict=json.loads(jp_data)
in_dict=json.loads(in_data)
# 获取trend key
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']
# 获取日期数据，用于x轴，取2020年（到315下标结束）
us_x_data=us_trend_data['updateDate'][:314]
jp_x_data=jp_trend_data['updateDate'][:314]
in_x_data=in_trend_data['updateDate'][:314]
# 获取确认数据，用于y轴，取2020年（到315下标结束）
us_y_data=us_trend_data['list'][0]['data'][:314]
jp_y_data=jp_trend_data['list'][0]['data'][:314]
in_y_data=in_trend_data['list'][0]['data'][:314]

# 生成图表
line=Line()     # 构建折线图对象
# 添加x轴数据
line.add_xaxis(us_x_data)    # x轴是公用的，所以使用一个国家的数据即可
# 添加y轴数据
line.add_yaxis("美国确诊人数",us_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数",jp_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数",in_y_data,label_opts=LabelOpts(is_show=False))
# 设置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title="2020美日印三国确诊人数对比折线图", pos_left="center",pos_bottom="1%"),    # 标题设置
)
# 调用render方法，生成图表
line.render()
# 关闭文件
f_us.close()
f_jp.close()
f_in.close()