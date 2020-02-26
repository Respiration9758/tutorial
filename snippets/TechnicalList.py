# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 18:26:55 2019

@author: Administrator
"""
import numpy as np
import pandas as pd


# [AR,BR]=ARBR(Open,High,Low,Close,Length)
# Open-开盘价序列,High-最高价序列,Low-最低价序列,Close-收盘价序列
# Length-计算AR和BR所考虑的时间周期，常用26个Bar
# AR-人气指标.BR-买卖意愿指标
def ARBR(Open, High, Low, Close, Length=26):
    AR = [];BR = []
    for i in range(len(Open)):
        if i < Length:
            arH = sum(High[0:i + 1])
            arO = sum(Open[0:i + 1])
            arL = sum(Low[0:i + 1])
        else:
            arH = sum(High[i - Length + 1:i + 1])
            arO = sum(Open[i - Length + 1:i + 1])
            arL = sum(Low[i - Length + 1:i + 1])
        if arO - arL == 0:
            ar = 100
        else:
            ar = (arH - arO) / (arO - arL) * 100
        AR.append(ar)

    BR.append(100)
    for i in range(1, len(High)):
        if i < Length:
            temp1 = sum([High[j] - Close[j - 1] for j in range(1, i)])  # 最高价减去昨天收盘价
            temp2 = sum([Close[j - 1] - Low[j] for j in range(1, i)])  # 昨天收盘价减去最低价
        else:
            temp1 = sum([High[j] - Close[j - 1] for j in range(1, i)])  # 最高价减去昨天收盘价
            temp2 = sum([Close[j - 1] - Low[j] for j in range(1, i)])  # 昨天收盘价减去最低价
        if temp2 == 0:
            br = 100
        else:
            br = temp1 / temp2 * 100
        BR.append(br)

    return (AR, BR)


# BIASValue=BIAS(Price,Length,Type)
# Price-计算BIAS所用的价格序列，常用收盘价
# Length-计算BIAS时考虑的Bar数，常用6、12和24
# Type-计算BIAS时所用的移动平均类型，如果Type等于0，则为简单移动平均，如果
# Type=1，则为指数移动平均，默认为简单移动平均
# BIASValue-乖离率指标
def BIAS(Price, Length, Type=0):
    BIASValue = []
    if Type == 0:
        MAValue = MA(Price, Length)
        for i in range(len(Price)):
            if i < Length:
                bias = (Price[i] - MAValue[0]) / MAValue[0] * 100
            else:
                bias = (Price[i] - MAValue[i - Length + 1]) / MAValue[i - Length + 1] * 100
            BIASValue.append(bias)

    if Type == 1:
        EMAValue = EMA(Price, Length)
        for i in range(len(Price)):
            if i < Length:
                bias = (Price[i] - EMAValue[0]) / EMAValue[0] * 100
            else:
                bias = (Price[i] - EMAValue[i - Length + 1]) / EMAValue[i - Length + 1] * 100
            BIASValue.append(bias)

    return BIASValue


# [UpperLine MiddleLine LowerLine]=BOLL(Price,Length,Width,Type)
# Price-价格序列，常用收盘价
# Length-计算移动平均的长度，常用20
# Width-计算布林线上轨和下轨的宽度，即多少个标准差，常用2
# Type-计算移动平均值的类型，0为简单移动平均，1为指数移动平均，默认为0
# UpperLine-上轨,MiddleLine-中轨,LowerLine-下轨
def BOLL(Price, Type=0, Length=20, Width=2):
    MiddleLine = []
    UpperLine = []
    LowerLine = []
    # 使用简单移动平均线
    if Type == 0:
        MiddleLine = MA(Price, Length)
        for i in range(len(Price)):
            if i < Length:
                upperLine = MiddleLine[i] + Width * np.std(Price[0:i + 1])
                lowerLine = MiddleLine[i] + Width * np.std(Price[0:i + 1])
            else:
                upperLine = MiddleLine[i] + Width * np.std(Price[i - Length:i + 1])
                lowerLine = MiddleLine[i] - Width * np.std(Price[i - Length:i + 1])
            UpperLine.append(upperLine)
            LowerLine.append(lowerLine)

    # 使用指数移动平均线
    if Type == 1:
        MiddleLine = EMA(Price, Length)
        for i in range(len(Price)):
            stan = []
            if i < Length:
                stan = [np.square(Price[j] - MiddleLine[0]) for j in range(i)]
            else:
                stan = [np.square(Price[j] - MiddleLine[i - Length]) for j in range(i - Length, i)]
            # for j in range(i-Length+1,i+1):
            #    stanDev += np.square(Price[j]-MiddleLine[i-Length+1])
            stanDev = sum(stan)
            StanDev = np.sqrt(stanDev / Length)
            upperLine = MiddleLine[i - Length + 1] + Width * StanDev
            lowerLine = MiddleLine[i - Length + 1] - Width * StanDev
            UpperLine.append(upperLine)
            LowerLine.append(lowerLine)

    return (UpperLine, MiddleLine, LowerLine)


# [DMAValue,AMAValue]=DMA(Price,FastLength,SlowLength,SmoothLength)
# Price-目标价格序列,FastLength-计算DMAValue时的短周期，常用10
# SlowLength-计算DMAValue时的长周期，常用50,SmoothLength-计算AMAValue时的周期，常用10
# DMAValue-短期均线和长期均线之差,AMAValue-DMAValue的移动平均
def DMA(Price, FastLength=10, SlowLength=50, SmoothLength=10):
    MAValueF = MA(Price, FastLength)
    MAValueS = MA(Price, SlowLength)
    DMAValue = [MAValueF[i] - MAValueS[i] for i in range(len(MAValueF))]
    AMAValue = MA(DMAValue, SmoothLength)

    return (DMAValue, AMAValue)


# DPOValue=DPO(Price,Length)
# Price-价格序列，常用收盘价序列,Length-20
# DPOValue-区间振荡指标
def DPO(Price, Length=10):
    DPOValue = []
    Offset = int(Length * 0.5 + 1)
    MAValue = MA(Price, Length)
    for i in range(len(Price)):
        if i < Offset:
            DPOValue.append(Price[i] - MAValue[0])
        else:
            DPOValue.append(Price[i] - MAValue[i - Offset])
    # DPOValue(Offset+1:end)=Price(Offset+1:end)-MAValue(1:end-Offset)
    return DPOValue


# EMAValue=EMA(Price,Length)
# Price-目标价格序列,Length-计算指数移动平均的周期,默认30
# EMAValue：指数移动平均值
def EMA(Price, Length=30):
    EMAValue = []
    K = 2 / (Length + 1)
    for i in range(len(Price)):
        if i == 0:
            ema = Price[i]
        else:
            ema = Price[i] * K + EMAValue[i - 1] * (1 - K)
        EMAValue.append(ema)

    return EMAValue


# [KValue,DValue,JValue]=KDJ(High,Low,Close,N,M,L,S)
# High-每个Bar的最高价序列,Low-每个Bar的最低价序列,Close-每个Bar的收盘价序列
# N-计算RSV时所考虑的周期,常用14,M-计算K值时的参数,常用3,L-计算D值时的参数,常用3
# S-计算J值时的参数,常用3,KValue-K值,DValue-D值,JValue-J值
def KDJ(High, Low, Close, N=14, M=3, L=3, S=3):
    KValue = [];
    DValue = [];
    JValue = []
    for i in range(len(High)):
        if i < N:
            LMin = min(Low[0:i + 1])  # N日的最低价
            HMax = max(High[0:i + 1])  # N日的最高价
        else:
            LMin = min(Low[i - N:i + 1])
            HMax = max(High[i - N:i + 1])

        if LMin != HMax:
            RSV = (Close[i] - LMin) / (HMax - LMin) * 100
        else:
            RSV = 0

        if i == 0:
            kValue = (M - 1) / M * 50 + 1 / M * RSV
            dValue = (L - 1) / L * 50 + 1 / L * kValue
        else:
            kValue = (M - 1) / M * KValue[i - 1] + 1 / M * RSV
            dValue = (L - 1) / L * DValue[i - 1] + 1 / L * kValue

        jValue = S * dValue - (S - 1) * kValue
        KValue.append(kValue);
        DValue.append(dValue);
        JValue.append(jValue)

    return (KValue, DValue, JValue)


# MAValue=MA(Price,Length)
# Price-目标价格序列(开盘价),Length-计算简单移动平均的周期
# MAValue：简单移动平均值
def MA(Price, Length=5):
    MAValue = []
    for i in range(len(Price)):
        if i < Length:
            # MAValue.append(Price[i])
            MAValue.append(sum(Price[0:i + 1]) / (i + 1))
        else:
            ma = sum(Price[i - Length + 1:i + 1]) / Length
            MAValue.append(ma)

    return MAValue


# [DIF,DEA,MACDValue]=MACD(Price,FastLength,SlowLength,DEALength)
# Price-目标价格序列,FastLength-计算DIF时的短周期，常用12
# SlowLength-计算DIF时的长周期，常用26,DEALength-计算DEA时的周期，常用9
# DIF-差离值（DIF）的计算： DIF = EMA12 - EMA26
# DEA-DIF的N日指数移动平均,MACDValue-2*（DIF-DEA）
def MACD(Price, FastLength=12, SlowLength=26, DEALength=9):
    #    DIF = EMA(Price,FastLength) - EMA(Price,SlowLength)
    FastEMA = EMA(Price, FastLength)
    SlowEMA = EMA(Price, SlowLength)
    DIF = [FastEMA[i] - SlowEMA[i] for i in range(len(FastEMA))]
    DEA = EMA(DIF, DEALength)
    MACDValue = [2 * (DIF[i] - DEA[i]) for i in range(len(DIF))]

    return MACDValue


# PSYValue=PSY(Price,Length)
# Price-价格序列，可以为Open、High、Low或Close，常用Close
# Length-计算时所考虑的周期，常用12个Bar
# PSYValue-心理线指标
def PSY(Price, Length=12):
    PSYValue = []
    for i in range(len(Price)):
        if i < Length:
            PSYValue.append(50)
        else:
            countP = 0
            for j in range(Length):
                if Price[i - j] > Price[i - j - 1]:
                    countP += 1
            psyValue = countP / Length * 100
            PSYValue.append(psyValue)

    return PSYValue


# WVADValue=WVAD(Open,High,Low,Close,Volume,Length)
# Open-开盘价序列,High-最高价序列,Low-最低价序列,Close-收盘价序列
# Volume-成交量序列,Length-考虑的周期，常用24个Bar
# WVADValue-威廉变异离散量
def WVAD(Open, High, Low, Close, Volume, Length=24):
    VADValue = []
    for i in range(len(Open)):
        if High[i] <= Low[i]:
            VADValue.append(0)
        else:
            VADValue.append((Close[i] - Open[i]) / (High[i] - Low[i]) * Volume[i])

    MAValue = MA(VADValue, Length)
    WVADValue = [wvas * Length / 1000 for wvas in MAValue]

    return WVADValue


# 添加麦克指标
# High-每个Bar的最高价序列,Low-每个Bar的最低价序列,Close-每个Bar的收盘价序列
# 初级压力——WR、中级压力——MR和强力压力——SR;初级支撑——WS、中级支撑——MS和强力支撑——SS
def MIKE(High, Low, Close, N=5):
    WR = [];
    MR = [];
    SR = []
    WS = [];
    MS = [];
    SS = []
    for i in range(len(Close)):
        H = High[i];
        L = Low[i];
        C = Close[i]
        TYP = (H + L + 2 * C) / 4
        if i < N:
            LN = min(Low[0:i + 1])  # N日的最低价
            HN = max(High[0:i + 1])  # N日的最高价
        else:
            LN = min(Low[i - N:i + 1])
            HN = max(High[i - N:i + 1])

        WR.append(TYP + (TYP - LN))
        MR.append(TYP + (HN - LN))
        SR.append(2 * HN - LN)
        WS.append(TYP - (HN - TYP))
        MS.append(TYP - (HN - LN))
        SS.append(2 * LN - HN)
    return (WR, MR, SR, WS, MS, SS)

def getData(df,technicalLists):
    Close = df['close'].values.tolist()
    Open = df['open'].values.tolist()
    High = df['high'].values.tolist()
    Low = df['low'].values.tolist()
    Volume = df['volume'].values.tolist()

    data =df[['close','open','high','low','volume']]
    for t in technicalLists:
        if t.interface=='MA5':
            MAValue = MA(Close,5)
            data['MA5'] = MAValue
        elif t.interface=='MA10':
            EMAValue = EMA(Close, 10)
            data['MA10'] = EMAValue
        elif t.interface=='MA20':
            EMAValue = EMA(Close, 20)
            data['MA20'] = EMAValue
        elif t.interface=='MA30':
            EMAValue = EMA(Close, 30)
            data['MA30'] = EMAValue
        elif t.interface == 'MA60':
            EMAValue = EMA(Close, 60)
            data['MA60'] = EMAValue
        elif t.interface == 'ARBR':
            AR, BR = ARBR(Open, High, Low, Close)
            data['AR'] = AR
            data['BR'] = BR
        elif t.interface == 'BIAS0':
            BIASValue0 = BIAS(Close, 6, 0)
            BIASValue012 = BIAS(Close, 12, 0)
            BIASValue024 = BIAS(Close, 24, 0)
            data['BIAS0'] = BIASValue0
            data['BIAS01'] = BIASValue012
            data['BIAS02'] = BIASValue024
        elif t.interface == 'BIAS1':
            BIASValue1 = BIAS(Close, 6, 1)
            BIASValue112 = BIAS(Close, 12, 1)
            BIASValue124 = BIAS(Close, 24, 1)
            data['BIAS1'] = BIASValue1
            data['BIAS11'] = BIASValue112
            data['BIAS12'] = BIASValue124
        elif t.interface == 'BOLL0':
            UpperLine0, MiddleLine0, LowerLine0 = BOLL(Close, 0)
            data['UL0'] = UpperLine0
            data['ML0'] = MiddleLine0
            data['LL0'] = LowerLine0
        elif t.interface == 'BOLL1':
            UpperLine1, MiddleLine1, LowerLine1 = BOLL(Close, 1)
            data['UL1'] = UpperLine1
            data['ML1'] = MiddleLine1
            data['LL1'] = LowerLine1
        elif t.interface == 'DMA':
            DMAValue, AMAValue = DMA(Close)
            data['DMA'] = DMAValue
            data['AMA'] = AMAValue
        elif t.interface == 'DPO':
            DPOValue = DPO(Close)
            data['DPO'] = DPOValue
        elif t.interface == 'EMA10':
            EMAValue = EMA(Close, 10)
            data['EMA10'] = EMAValue
        elif t.interface == 'EMA20':
            EMAValue = EMA(Close, 20)
            data['EMA20'] = EMAValue
        elif t.interface == 'EMA30':
            EMAValue = EMA(Close, 30)
            data['EMA30'] = EMAValue
        elif t.interface == 'KDJ':
            KValue, DValue, JValue = KDJ(High, Low, Close)
            data['KValue'] = KValue
            data['DValue'] = DValue
            data['JValue'] = JValue
        elif t.interface == 'KDJ':
            MACDValue = MACD(Close)
            data['MACD'] = MACDValue
        elif t.interface == 'PSY':
            PSYValue = PSY(Close)
            data['PSY'] = PSYValue
        elif t.interface == 'WVAD':
            WVADValue = WVAD(Open, High, Low, Close, Volume)
            data['WVAD'] = WVADValue
        elif t.interface == 'MIKE':
            WR, MR, SR, WS, MS, SS = MIKE(High, Low, Close)
            data['WR'] = WR
            data['MR'] = MR
            data['SR'] = SR
            data['WS'] = WS
            data['MS'] = MS
            data['SS'] = SS

    return data




