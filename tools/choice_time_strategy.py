import numpy as np
import pandas as pd
import tushare as ts
# import tools.dataProcess
def trend_trace_MA(filePath, snum, lnum):
    """
    根据股票代码，选择一定时间范围内的历史交易数据，根据给出的短期和长期均线的时间间
    隔计算均线，最终返回相关历史数据以及买卖点。

    :param scode: 股票代码
    :param startTime: 历史数据的开始时间
    :param endTime: 历史数据的结束时间
    :param snum: 短期均线长度
    :param lnum: 长期均线长度
    :return: bs_points： 代表判断的买卖点

    """
    shdata = pd.read_csv(filePath, index_col='date')


    golden_cross = []
    death_cross = []

    # 求金叉死叉的方法二
    ser1 = shdata['MA'+str(snum)] < shdata['MA'+str(lnum)]
    ser2 = shdata['MA'+str(snum)] >= shdata['MA'+str(lnum)]
    # One-dimensional ndarray with axis labels (including time series).

    death_cross = shdata[ser1 & ser2.shift(1)].index
    golden_cross = shdata[-(ser1 | ser2.shift(1))].index

    ser1 = pd.Series(1, index=golden_cross)
    ser2 = pd.Series(-1, index=death_cross)
    bs_points = ser1.append(ser2).sort_index()

    return  bs_points


# shdata, bs_points = trend_trace_MA('600519','1988-01-01','2020-01-21',5, 20)
#
# shdata['label'] = bs_points
#
# shdata.dropna(axis=0, how='any', inplace=True)