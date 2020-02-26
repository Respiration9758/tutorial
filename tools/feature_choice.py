import numpy as np
import pandas as pd
from sklearn.decomposition import PCA


# 技术指标特征选择方法PCA
def TI_PCA(data):
    """

    :param data: 输入特征矩阵，ndarray
    :return: 输出特征选择后的特征矩阵
    """
    return PCA(n_components=8).fit_transform(data)