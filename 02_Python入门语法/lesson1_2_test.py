
# 股票计算小程序
name = input("Please input name:")
stock_price = float(input("Please input stock_price:"))
stock_code = input("Please input stock_code:")
stock_price_daily_growth_factor = float(input("Please input stock_price_daily_growth_factor:"))
stock_price_growth_days = int(input("Please input stock_price_growth_days:"))
print(
    f"公司：{name},股票代码：{stock_code},当前股票：{stock_price}\n每日增长系数是：{stock_price_daily_growth_factor},经过{stock_price_growth_days}天的增长后，股价达到了：{stock_price * (stock_price_daily_growth_factor ** stock_price_growth_days)}")
print("每日增长系数是：%.1f,经过%d天的增长后，股价达到了：%.2f" % (
    stock_price_daily_growth_factor, stock_price_growth_days,
    stock_price * (stock_price_daily_growth_factor ** stock_price_growth_days)))
print(f"公司：{name},股票代码：{stock_code},当前股票：{stock_price}\n",
      "每日增长系数是：%.1f,经过%d天的增长后，股价达到了：%.2f" % (
          stock_price_daily_growth_factor, stock_price_growth_days,
          stock_price * (stock_price_daily_growth_factor ** stock_price_growth_days)))

# 欢迎登陆小程序
user_name = input("请输入用户名称：")
user_type = input("请输入用户类型：")
# 三种方式
print("您好：%s，您是尊贵的：%s 用户，欢迎您的光临。" % (user_name, user_type))
print(f"您好：{user_name}，您是尊贵的：{user_type} 用户，欢迎您的光临。")
print("您好：" + user_name + "，您是尊贵的：" + user_type + " 用户，欢迎您的光临。")
