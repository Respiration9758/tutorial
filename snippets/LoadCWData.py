import numpy as np
import pandas as pd
import tushare as ts

def getCWData(Year,Number,startDate,endDate):
    # 获取沪深300成分股及权重
    stocks = ts.get_hs300s()
    print(type(stocks))
    stocks = stocks.drop("date", axis=1)
    stocks = stocks.set_index('code')

    #获取2014年第3季度的业绩报表数据
    YeJi = ts.get_report_data(Year, Number)
    YeJi = YeJi.drop('eps_yoy', axis=1)
    YeJi = YeJi.drop('bvps', axis=1)
    YeJi = YeJi.drop('epcf', axis=1)
    YeJi = YeJi.drop('profits_yoy', axis=1)
    YeJi = YeJi.drop('distrib', axis=1)
    YeJi = YeJi.drop('report_date', axis=1)
    YeJi = YeJi.drop('name', axis=1)
    # 获取2014年第3季度的盈利能力数据
    YingLi = ts.get_profit_data(Year, Number)
    YingLi = YingLi.drop('name', axis=1)
    YingLi = YingLi.drop('roe', axis=1)
    YingLi = YingLi.drop('eps', axis=1)
    YingLi = YingLi.drop('net_profits', axis=1)
    # 获取2014年第3季度的营运能力数据
    YunYing = ts.get_operation_data(Year, Number)
    YunYing = YunYing.drop('name', axis=1)
    # 获取2014年第3季度的成长能力数据
    ChengZhang = ts.get_growth_data(Year, Number)
    ChengZhang = ChengZhang.drop('name', axis=1)
    # 获取2014年第3季度的偿债能力数据
    ChangZhai = ts.get_debtpaying_data(Year, Number)
    ChangZhai = ChangZhai.drop('name', axis=1)
    # 获取2014年第3季度的现金流量数据
    XianJin = ts.get_cashflow_data(Year, Number)
    XianJin = XianJin.drop('name', axis=1)


    result1 = pd.merge(stocks, YeJi, on='code')
    result = PreStocks(result1)
    # result = YeJi
    result2 = pd.merge(result, YingLi, on='code')
    result = PreStocks(result2)
    result3 = pd.merge(result, YunYing, on='code')
    result = PreStocks(result3)
    result4 = pd.merge(result, ChengZhang, on='code')
    result = PreStocks(result4)
    result5 = pd.merge(result, ChangZhai, on='code')
    result = PreStocks(result5)
    result6 = pd.merge(result, XianJin, on='code')
    result = PreStocks(result6)

    # 删除所有为NaN的行
    result = result.dropna(axis=0, how='any')




    stock = result['code'].values.tolist()
    #startDate = '2018-01-01'
    #endDate = '2018-03-31'
    datas = []#获取股票对应日期范围内的收盘价序列
    for i in stock:
        data = ts.get_hist_data(str(i), start=startDate, end=endDate)
        data.sort_index(inplace=True)  # 由于下载的数据倒序排序，本方法重新按列索引排序
        closes = data['close'].values.tolist()
        datas.append((i, closes))
    for i in [0.1,0.2,0.3]:
        label = []
        stockIns = i
        for i in datas:
            closes = i[1]
            l = 0
            for d in range(len(closes)):
                if (closes[d] - closes[0]) / closes[0] <= -float(stockIns):
                    if l == -1 or l == 0:
                        l = -1#股票趋势下跌
                    else:
                        l = 0
                elif (closes[d] - closes[0]) / closes[0] >= float(stockIns):
                    if l == 1 or l == 0:
                        l = 1#股票趋势上涨
                    else:
                        l = 0
            label.append(l)
        result['label3_'+str(i*10)] = label
    return result

def PreStocks(result):
    #读取DatFrame中某一特征某一行的值
    #data['code'][0]
    #去除重复的行，以code为判断标准
    #定义一个记录的列表
    listTemp = []
    num = result.shape[0]
    for i in range(num):
        code = result['code'][i]
        if code in listTemp:
            result = result.drop([i])
        else:
            listTemp.append(code)
    return result