import pandas as pd
import numpy as np
from sklearn import preprocessing
from collections import Counter
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

def load_data(tdlLists):
    # FileName = '../data/hs300CB2016_2_label.csv'
    data1 = pd.read_csv(tdlLists[0], parse_dates=True)  # 读文件不成功
    if len(tdlLists)>1:
        for i in range(1,len(tdlLists)):
            dataTemp =  pd.read_csv(tdlLists[1], parse_dates=True)  # 读文件不成功
            data1.append(dataTemp)

    data = data1.drop(['code', 'name', 'weight', 'Unnamed: 0'], 1)
    # 将data中包含的‘--’替换为0
    d = data.replace('--', 0)
    # x = d.drop(['label3_1','label3_2','label3_3'], 1)
    # x = x.dropna(axis=0,how='any')
    X = np.array(d.drop(['label3_1', 'label3_2', 'label3_3'], 1))

    X = preprocessing.scale(X)  # 对数据特征正则化
    X = PCABP(X)

    # y = np.array([d['label3'],d['label3_1']]).T
    y = np.array(d['label3_2'])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    return (X_train, X_test, y_train, y_test)

def PCABP(X):
    pca = PCA(n_components=14)
    newX = pca.fit_transform(X)
    return newX


class Config:
    nn_input_dim = 14  # 数组输入的维度是2（x,y两个坐标当然是二维啊）
    nn_output_dim = 3  # 数组输出的维度是2（分为两类当然是二维啊）
    epsilon = 0.01  # 梯度下降学习步长
    reg_lambda = 0.01  # 修正的指数?


def build_model(X, y, nn_hdim, num_passes=2000, print_loss=False):
    Config.nn_input_dim = 14  # 数组输入的维度是2（x,y两个坐标当然是二维啊）
    Config.nn_output_dim = 3  # 数组输出的维度是2（分为两类当然是二维啊）
    Config.epsilon = 0.01  # 梯度下降学习步长
    Config.reg_lambda = 0.01  # 修正的指数?

    num_examples = len(X)
    np.random.seed(0)  # 初始化权值和偏置
    W1 = np.random.randn(Config.nn_input_dim, nn_hdim) / np.sqrt(Config.nn_input_dim)
    b1 = np.zeros((1, nn_hdim))
    W2 = np.random.randn(nn_hdim, Config.nn_output_dim) / np.sqrt(nn_hdim)
    b2 = np.zeros((1, Config.nn_output_dim))
    model = {}

    for i in range(0, num_passes):
        z1 = X.dot(W1) + b1  # 输入层向隐藏层正向传播
        a1 = np.tanh(z1)  # 隐藏层激活函数使用tanh = (exp(x) - exp(-x)) / (exp(x) + exp(-x))
        z2 = a1.dot(W2) + b2  # 隐藏层向输出层正向传播
        exp_scores = np.exp(z2)  # 这两步表示输出层的激活函数为softmax函数哦
        probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

        delta3 = probs
        # 下面这才是delta3，为损失函数对z2求偏导数，y-y^
        delta3[range(num_examples), y] -= 1
        dW2 = (a1.T).dot(delta3)  # 损失函数对w2的偏导数
        db2 = np.sum(delta3, axis=0, keepdims=True)  # 损失函数对b2的偏导数
        delta2 = delta3.dot(W2.T) * (1 - np.power(a1, 2))  # 损失函数对z1的偏导数
        dW1 = np.dot(X.T, delta2)  # 损失函数对w1的偏导数
        db1 = np.sum(delta2, axis=0)  # 损失函数对b1的偏导数
        # 个人认为下面两行代码完全没有必要存在
        dW2 += Config.reg_lambda * W2  # w2梯度增量的修正  屁话
        dW1 += Config.reg_lambda * W1  # w1梯度增量的修正  屁话
        # 更新权值和偏置
        W1 += -Config.epsilon * dW1
        b1 += -Config.epsilon * db1
        W2 += -Config.epsilon * dW2
        b2 += -Config.epsilon * db2

        model = {'W1': W1, 'b1': b1, 'W2': W2, 'b2': b2}

    return model


def predict(model, x):
    # 这是字典啊
    W1, b1, W2, b2 = model['W1'], model['b1'], model['W2'], model['b2']
    z1 = x.dot(W1) + b1  # 输入层向隐藏层正向传播
    a1 = np.tanh(z1)  # 隐藏层激活函数使用tanh = (exp(x) - exp(-x)) / (exp(x) + exp(-x))
    z2 = a1.dot(W2) + b2  # 隐藏层向输出层正向传播
    exp_scores = np.exp(z2)  # 这两步表示输出层的激活函数为softmax函数哦
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    return np.argmax(probs, axis=1)

def main():
    X_train, X_test, y_train, y_test = load_data('../data/')
    model = build_model(X_train, y_train, 64)  # 8=nn_hdim,表示隐藏层节点个数

    # joblib.dump(model,'CW2017Frist_BP_train_model.m')#保存训练的模型
    # clf=joblib.load('filename.pkl')#加载保存的训练模型

    predicted_class = predict(model, X_test)
    #    hidden_layer = np.maximum(0, np.dot(X, W) + b)
    #    scores = np.dot(hidden_layer, W2) + b2
    #    predicted_class = np.argmax(scores, axis=1)
    print('training accuracy: %.3f' % (np.mean(predicted_class == y_test)))


def strategyTrain(algorithm,tdlLists):
    X_train, X_test, y_train, y_test = load_data(tdlLists)
    if algorithm == 'BP神经网络':
        # X_train, X_test, y_train, y_test = load_data('../data/')
        model = build_model(X_train, y_train, 64)  # 8=nn_hdim,表示隐藏层节点个数
        # joblib.dump(model,'CW2017Frist_BP_train_model.m')#保存训练的模型
        # clf=joblib.load('filename.pkl')#加载保存的训练模型
        predicted_class = predict(model, X_test)
        print(predicted_class)
        accuracy = np.mean(predicted_class == y_test)
        return (model,accuracy,y_test,predicted_class)
    return

from sklearn.externals import joblib
def load_dataPre(tdlLists):
    # FileName = '../data/hs300CB2016_2_label.csv'
    data1 = pd.read_csv(tdlLists[0], parse_dates=True)  # 读文件不成功
    if len(tdlLists)>1:
        for i in range(1,len(tdlLists)):
            dataTemp =  pd.read_csv(tdlLists[1], parse_dates=True)  # 读文件不成功
            data1.append(dataTemp)

    data = data1.drop(['code', 'name', 'weight', 'Unnamed: 0'], 1)
    # 将data中包含的‘--’替换为0
    d = data.replace('--', 0)
    # x = d.drop(['label3_1','label3_2','label3_3'], 1)
    # x = x.dropna(axis=0,how='any')
    X = np.array(data)

    X = preprocessing.scale(X)  # 对数据特征正则化
    X = PCABP(X)

    # y = np.array([d['label3'],d['label3_1']]).T
    # y = np.array(d['label3_2'])
    return X

def strategyPre(filePath,tdlLists):
    X = load_dataPre(tdlLists)
    # joblib.dump(model,'CW2017Frist_BP_train_model.m')#保存训练的模型
    clf=joblib.load('filename.pkl')#加载保存的训练模型
    predicted_class = predict(clf, X)
    print(predicted_class)
    return predicted_class
