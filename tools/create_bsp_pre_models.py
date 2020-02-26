from tools.choice_time_strategy import trend_trace_MA
import tools.feature_choice
import pandas as pd
import numpy as np

def create_bsp_p_model(filePath, algorithm, bsp_r, f_c, period):
    """

    :param filePath: 测试训练数据集的路径
    :param algorithm: 选择预测
    :param bsp_r: 选择买卖点识别方法
    :param f_c: 特征选择方法
    :param period: 每一个实例数据的间隔
    :return: 预测准确率，测试数据的预测结果保存路径
    """
    tidata_df = pd.read_csv(filePath, index_col='date', parse_dates=True)

    # 添加买卖点标签
    if bsp_r == 1:
        bs_points = trend_trace_MA(filePath, 5, 20)
        tidata_df['label'] = bs_points
        # tidata_df.dropna(axis=0, how='any', inplace=True)


    # 整理训练集



    # 特征工程


    # 训练模型


    # 返回值

