def norm_province(data):
    """
    :param data: 传入pyecharts地图模块中的data数据
    :return: 返回校正后的data数据
    """
    province = ("新疆维吾尔自治区", "西藏自治区", "宁夏回族自治区", "广西壮族自治区", "内蒙古自治区", "澳门特别行政区",
                "香港特别行政区", "重庆市", "北京市", "天津市", "上海市", "甘肃省", "青海省", "四川省", "云南省",
                "贵州省", "陕西省", "湖南省", "湖北省", "河南省", "山西省", "河北省", "辽宁省", "吉林省", "黑龙江省",
                "山东省", "江苏省", "安徽省", "浙江省", "江西省", "福建省", "台湾省", "广东省", "海南省")
    norm_data = []
    for x in data:
        x=list(x)
        for area in province:
            if x[0] in area:
                x[0]=area
                x=tuple(x)
                norm_data.append(x)
    return norm_data


