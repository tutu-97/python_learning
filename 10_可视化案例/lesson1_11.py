
# 数据可视化-地图可视化
# 基础地图使用
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 准备地图对象
china_map=Map()
# 准备数据   要写正确的省份和市，eg：北京要写北京市，四川要写四川省，内蒙古要写内蒙古自治区
data=[("北京市",99),("湖南省",299),("台湾省",399),("安徽省",499),("湖北省",699),("重庆市",99),("内蒙古自治区",233)]
# 添加数据
china_map.add("测试地图", data, "china")

# 颜色代码 在线懒人工具 ab173->前端->rgb颜色对照表

# 设置全局选项
china_map.set_global_opts(visualmap_opts=VisualMapOpts(is_show=True, is_piecewise=True, pieces=[
        {"min":1,"max":9,"label":"1-9人","color":"#ccffff"},
        {"min":10,"max":99,"label":"10-99人","color":"#ffff99"},
        {"min":100,"max":499,"label":"99-499人","color":"#ff9966"},
        {"min":500,"max":999,"label":"499-999人","color":"#ff6666"},
        {"min":1000,"max":9999,"label":"1000-9999人","color":"#cc3333"},
        {"min":10000,"label":"10000以上","color":"#990033"}
    ])
)
# 绘图
china_map.render("ChinaMap.html")

import json

# 疫情地图-国内疫情地图
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

from basics.stage1.norm_province import norm_province

# 读取数据文件
f=open("D:\个人\\learning\\python\可视化案例数据\地图数据\疫情.txt","r",encoding="UTF-8")
ch_data=f.read()
# 关闭文件
f.close()
# 取到各省数据
# 将字符串json转换成python的字典
data_dict=json.loads(ch_data)   # 基础数据
# 从字典中取出省份的数据
province_data_list=data_dict["areaTree"][0]["children"]
# 组装每个省份和确诊人数为元组，并各个省的数据都封装入列表内
data_list=[]     # 绘图需要用的数据列表
for province_data in province_data_list:
    province_name=province_data["name"]
    province_confirm=province_data["total"]["confirm"]
    data_list.append((province_name, province_confirm))
    # province_data=(province_name,province_confirm)
    # province_data_list[province_data_list.index(province_data)]=province_data
# 创建地图对象
map=Map()
# 添加数据
data_list=norm_province(data_list)
map.add("各省份确诊人数",data_list,"china")
# 设置全局配置,定制分段的视觉映射
map.set_global_opts(visualmap_opts=VisualMapOpts(
    is_show=True,         # 是否显示
    is_piecewise=True,    # 是否分段
    pieces=[
    {"min":1,"max":9,"label":"1-9人","color":"#ccffff"},
    {"min":10,"max":99,"label":"10-99人","color":"#ffff99"},
    {"min":100,"max":499,"label":"99-499人","color":"#ff9966"},
    {"min":500,"max":999,"label":"499-999人","color":"#ff6666"},
    {"min":1000,"max":9999,"label":"1000-9999人","color":"#cc3333"},
    {"min":10000,"label":"10000以上","color":"#990033"}
    ])
)
# 绘图
map.render("中国疫情地图.html")

# 省级疫情地图
import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
# 读取文件
f=open("D:\个人\\learning\\python\可视化案例数据\地图数据\疫情.txt","r",encoding="UTF-8")
data=f.read()
# 关闭文件
f.close()
# 获取河南省数据
# json数据转换为python字典
data_dict=json.loads(data)
# 取到河南省数据
cities_data=data_dict["areaTree"][0]["children"][3]["children"]
data_list=[]
for city_data in cities_data:
    cities_name=city_data["name"]+"市"
    cities_confirm=city_data["total"]["confirm"]
    data_list.append((cities_name,cities_confirm))
# 构建地图
map=Map()
map.add("河南省确诊人数",data_list,"河南")
# 设置全局选项
map.set_global_opts(
    # title_opts=TitleOpts(title="河南省确诊人数地图",pos_left="center",pos_top="1%"),
    visualmap_opts=VisualMapOpts(
    is_show=True,         # 是否显示
    is_piecewise=True,    # 是否分段
    pieces=[
    {"min":1,"max":9,"label":"1-9人","color":"#ccffff"},
    {"min":10,"max":99,"label":"10-99人","color":"#ffff99"},
    {"min":100,"max":499,"label":"99-499人","color":"#ff9966"},
    {"min":500,"max":999,"label":"499-999人","color":"#ff6666"},
    {"min":1000,"max":9999,"label":"1000-9999人","color":"#cc3333"},
    {"min":10000,"label":"10000以上","color":"#990033"}
    ])
)
# 绘图
map.render("河南省确诊人数地图.html")