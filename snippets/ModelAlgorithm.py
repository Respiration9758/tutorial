import pandas as pd
import numpy as np
import datetime
import math
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn import neighbors
from sklearn.tree import DecisionTreeRegressor
from sklearn import svm
from sklearn import ensemble

def load_data(fileName,forecast_out=0):
    #fileName = '../data/600015.XSHG.csv'
    df = pd.read_csv(fileName, index_col='date', parse_dates=True)  # 读入csv的数值字符为数值型

    df['HH_PCH'] = (df['high'] - df['open']) / df['close'] * 100.0
    df['HL_PCT'] = (df['open'] - df['low']) / df['close'] * 100.0
    df['PCT_change'] = (df['close'] - df['open']) / df['open'] * 100.0

    df = df[['close', 'HL_PCT', 'PCT_change', 'volume']]

    # 对空数据进行处理，同时对Close的股票value进行预测，
    # forecast_out表示往后预测的天数
    forecast_col = 'close'
    df.fillna(value=-99999, inplace=True)
    if forecast_out == 0:
        forecast_out = int(math.ceil(0.01 * len(df)))

    df['label'] = df[forecast_col].shift(-forecast_out)
    df['closeT'] = df['close']
    print(df.shape)
    print(df.tail())
    X = np.array(df.drop(['label','closeT'], 1))

    X = preprocessing.scale(X)

    X_lately = X[-forecast_out:]
    X = X[:-forecast_out]
    df.dropna(inplace=True)

    print(X)
    print(X_lately)
    y = np.array([df['label'],df['closeT']]).T
    print(X.shape)
    print(y.shape)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    return (X_train, X_test, y_train, y_test)

def try_different_method(clf,X_train, X_test, y_trainT, y_testT):
    y_train = y_trainT[:,0]
    y_test = y_testT[:,0]
    clf.fit(X_train,y_train)
    accuracy = clf.score(X_test, y_test)
    result = clf.predict(X_test)
    # 使用自带的样式进行美化
    # plt.style.use('ggplot')
    # plt.figure()
    # plt.plot(np.arange(len(result)), y_test, 'go-', label='true value')
    # plt.plot(np.arange(len(result)), result, 'ro-', label='predict value')
    # plt.title('accuracy: %f' % accuracy)
    # plt.legend()
    # plt.show()
    y_testOld = y_testT[:,1]
    r1,r2,r3 = ifTrend(y_testOld,y_test,result)
    return accuracy,y_test,result,r1,r2,r3

def ifTrend(y_testOld,y_test,result):
    trendT1 = []
    trendP1 = []
    trendT2 = []
    trendP2 = []
    trendT3 = []
    trendP3 = []
    for i in range(len(y_test)):
        trendT1.append(ifResult(y_test[i],y_testOld[i],0.1))
        trendP1.append(ifResult(result[i], y_testOld[i], 0.1))
        trendT2.append(ifResult(y_test[i], y_testOld[i], 0.2))
        trendP2.append(ifResult(result[i], y_testOld[i], 0.2))
        trendT3.append(ifResult(y_test[i], y_testOld[i], 0.3))
        trendP3.append(ifResult(result[i], y_testOld[i], 0.3))
    r1 = accuracy_score(trendT1,trendP1)
    r2 = accuracy_score(trendT2,trendP2)
    r3 = accuracy_score(trendT3,trendP3)
    return r1,r2,r3

def ifResult(t,p,num):
    if (p - t) / t > num:
        return 1
    elif (p - t) / t < -num:
        return -1
    else:
        return 0

def modelAlgorithm(fileName,forecast_out,jiekou):
    X_train, X_test, y_train, y_test = load_data(fileName,forecast_out)
    if jiekou == 'LR':
        clf = LinearRegression()
    elif jiekou == 'KNN':
        clf = neighbors.KNeighborsRegressor()
    elif jiekou == 'DTR':
        clf = DecisionTreeRegressor()
    elif jiekou =='SVM':
        clf = svm.SVR()
    elif jiekou == 'RFR':
        clf = ensemble.RandomForestRegressor(n_estimators=20)  # 这里使用20个决策树
    elif jiekou == 'AdaBoost':
        clf = ensemble.AdaBoostRegressor(n_estimators=50)
    elif jiekou == 'GBRT':
        clf = ensemble.GradientBoostingRegressor(n_estimators=100)  # 100个弱学习器
    else:
        clf = LinearRegression()

    accuracy, y_test, result,r1,r2,r3 = try_different_method(clf,X_train, X_test, y_train, y_test)
    return (clf,accuracy,y_test,result,r1,r2,r3)

