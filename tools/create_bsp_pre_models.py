from tools.choice_time_strategy import trend_trace_MA
import tools.feature_choice
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import sklearn

def create_bsp_p_model(filePath, algorithm, bsp_r, f_c, period):
    """

    :param filePath: 测试训练数据集的路径
    :param algorithm: 选择预测
    :param bsp_r: 选择买卖点识别方法
    :param f_c: 特征选择方法
    :param period: 每一个实例数据的间隔
    :return: 预测准确率，测试数据的预测结果保存路径
    """
    tidata_df = pd.read_csv(filePath, index_col='date')
    print("*********A")
    print(tidata_df.info())

    # 添加买卖点标签
    if bsp_r == 1:
        bs_points = trend_trace_MA(filePath, 5, 20)


    tidata_df['label'] = bs_points
    tidata_df.fillna(0, inplace=True)


    # 整理训练集(用periods天的数据预测下一天的数据)

    for i in range(tidata_df.shape[0] - period+1):
        if i == 0:
            train = tidata_df.iloc[i:i+period,:-1].values.reshape(1,-1)
        else:
            train = np.concatenate((train, tidata_df.iloc[i:i+period,:-1].values.reshape(1,-1)), axis=0)

    # train 数组

    train = np.concatenate((train, tidata_df.iloc[period-1:,-1].values.reshape(-1,1)), axis=1)

    train_df = pd.DataFrame(train,index=tidata_df.iloc[period-1:,0].index)
    print((train_df.iloc[:,-1]==1).sum())
    print((train_df.iloc[:,-1]==0).sum())
    print((train_df.iloc[:,-1]==-1).sum())
    # 将所有数据对齐（非均衡数据处理）
    num_1 = (train_df.iloc[:,-1]==1).sum()
    num_0 = (train_df.iloc[:,-1]==0).sum()
    num_m1 = (train_df.iloc[:, -1] == -1).sum()
    min_num = min(num_0,num_1,num_m1)

    df1 = train_df.loc[train_df.iloc[:, -1] == 1]
    df2 = train_df.loc[train_df.iloc[:, -1] == -1]
    df3 = train_df.loc[train_df.iloc[:, -1] == 0]
    df1 = df1.sample(min_num)
    df2 = df2.sample(min_num)
    df3 = df3.sample(min_num)

    train_df = pd.concat([df1, df2])
    train_df = pd.concat([train_df, df3])
    train_df.sort_index(inplace=True)



    # 特征工程
    if f_c == 1 :
        train = tools.feature_choice.TI_PCA(train_df.iloc[:,:-1])




    # train_data
    train_data = pd.DataFrame(train, index=train_df.index)
    # print(train_data)


    # 训练模型
    x_train, x_test, y_train, y_test = train_test_split(train_data
                                                        , train_df.iloc[:,-1], test_size=0.2)
    if algorithm == 1:
        clf = sklearn.ensemble.RandomForestClassifier(n_estimators=300)

    x_test.sort_index(inplace=True)
    y_test.sort_index(inplace=True)
    clf.fit(x_train, y_train)
    y_pre = clf.predict(x_test)
    y_pre = pd.Series(y_pre, index=y_test.index)

    acc = clf.score(x_test,y_test)



    # 返回值
    return clf,acc, y_pre

