# -*- coding: utf-8 -*-
import os
import akshare as ak
import pandas as pd
from datetime import datetime

print("STOCK600513 股票分析工具")

stock_code = "600513"
data_file = stock_code + "_data.csv"
start_date = "20230101"
end_date = datetime.now().strftime("%Y%m%d")

def check_data():
    return os.path.exists(data_file)

def download_data():
    try:
        print("正在下载数据，请稍候...")
        stock_zh_a_hist_df = ak.stock_zh_a_hist(
            symbol=stock_code,
            period="daily",
            start_date=start_date,
            end_date=end_date,
            adjust="qfq"
        )
        stock_zh_a_hist_df.to_csv(data_file, index=False, encoding="utf-8-sig")
        print("数据下载成功")
        return True
    except Exception as e:
        print("数据下载失败:", str(e))
        return False

# 检查数据
print("检查数据...")
has_data = check_data()
if has_data:
    print("本地存在交易数据文件")
    df = pd.read_csv(data_file, encoding="utf-8-sig")
    print("数据文件包含", len(df), "条记录")
    print("数据时间范围:", df.iloc[0]["日期"], "到", df.iloc[-1]["日期"])
else:
    print("本地不存在交易数据文件，开始下载...")
    download_data()