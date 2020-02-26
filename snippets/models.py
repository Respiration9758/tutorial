# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.db import models

# Create your models here.
from django.db import models
import datetime
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())
Technical = ['均线型','成交量型','能量型','趋势型','超买超卖型','路径型','其他型']
TechnicalType = sorted((item, item) for item in Technical)

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE,related_name='snippets')
    highlighted = models.TextField()

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
	    """
	    使用pygments来创建高亮的HTML代码。
	    """
	    lexer = get_lexer_by_name(self.language)
	    linenos = self.linenos and 'table' or False
	    options = self.title and {'title': self.title} or {}
	    formatter = HtmlFormatter(style=self.style, linenos=linenos,
	                              full=True, **options)
	    self.highlighted = highlight(self.code, lexer, formatter)
	    super(Snippet, self).save(*args, **kwargs)

class Zixun(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    category = models.TextField(default='')
    source = models.TextField(default='')
    update_time = models.TextField(default='')
    see_times = models.TextField(default='')
    publish_status = models.IntegerField(default=0)

    class Meta:
        ordering = ('created',)

class Picture(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    category = models.TextField(default='')
    isComment = models.BooleanField(default=False)
    publish_time = models.TextField(default='')
    content = models.TextField(default='')
    picture_list = models.TextField(default='')

    class Meta:
        ordering = ('created',)
        
class SS(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    qq = models.TextField(default='')
    wechat = models.TextField(default='')
    alipay = models.TextField(default='')
    buy_time = models.TextField(default='')
    end_time = models.TextField(default='')
    ss_ip = models.TextField(default='')
    ss_port = models.TextField(default='')
    ss_passwd = models.TextField(default='')
    ss_encry = models.TextField(default='aes-256-cfb')
    isExpired = models.BooleanField(default=False)
    note = models.TextField(default='')

    class Meta:
        ordering = ('created',)

#股票表
class Stock(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=100,default='')
    name = models.CharField(max_length=100, blank=True, default='')#blank=true允许为空
    industry = models.CharField(max_length=100, blank=True, default='')
    area = models.CharField(max_length=100, blank=True, default='')
    timeToMarket = models.TextField(default='')
    pe = models.DecimalField(max_digits=25, decimal_places=3,blank=True,null=True)
    outstanding = models.DecimalField(max_digits=25, decimal_places=3,blank=True,null=True)
    totals = models.DecimalField(max_digits=25, decimal_places=3,blank=True,null=True)
    totalsAssets = models.DecimalField(max_digits=25, decimal_places=3,blank=True,null=True)
    isExpired = models.BooleanField(default=False)
    note = models.TextField(default='')
    highlighted = models.TextField()

    class Meta:
        ordering = ('created',)

    # def save(self, *args, **kwargs):
    #     """
    #     使用pygments来创建高亮的HTML代码。
    #     """
    #     lexer = get_lexer_by_name(self.language)
    #     linenos = self.linenos and 'table' or False
    #     options = self.title and {'title': self.title} or {}
    #     formatter = HtmlFormatter(style=self.style, linenos=linenos,
    #                               full=True, **options)
    #     self.highlighted = highlight(self.code, lexer, formatter)
    #     super(Snippet, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.code+'-'+self.name+'-'+self.industry+'-'+self.area

#股票历史数据表
class StockData(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    stock = models.ForeignKey(Stock,on_delete=models.CASCADE)
    buy_time = models.TextField(default='')
    end_time = models.TextField(default='')
    number = models.IntegerField(blank=True,null=True)
    filePath = models.CharField(max_length=250,default='')
    isExpired = models.BooleanField(default=False)
    note = models.TextField(default='')

    class Meta:
        ordering = ('created',)

#股票财务数据表
class StockCWData(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')  # blank=true允许为空
    year = models.CharField(max_length=100, default='')
    quarter = models.CharField(max_length=100, default='')#季度
    number = models.IntegerField(blank=True, null=True)
    dimension = models.IntegerField(blank=True, null=True)  # 特征维度
    filePath = models.CharField(max_length=250, default='')
    isExpired = models.BooleanField(default=False)
    note = models.TextField(default='')
    startDate = models.TextField(default='')
    endDate = models.TextField(default='')
    KY1 = models.CharField(max_length=100, default='')
    KY2 = models.CharField(max_length=100, default='')
    KY3 = models.CharField(max_length=100, default='')

    class Meta:
        ordering = ('created',)

#股票技术指标表
class TechnicalList(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')  # blank=true允许为空
    nickname = models.CharField(max_length=100, default='')
    tType = models.CharField(default='均线型', max_length=100)
    interface = models.CharField(max_length=100, default='')
    parameter1 = models.CharField(max_length=100, default='')
    parameter2 = models.CharField(max_length=100, default='')
    parameter3 = models.CharField(max_length=100, default='')
    parameter4 = models.CharField(max_length=100, default='')
    parameter5 = models.CharField(max_length=100, default='')
    isExpired = models.BooleanField(default=False)
    note = models.TextField(default='')
    KY1 = models.CharField(max_length=100, default='')
    KY2 = models.CharField(max_length=100, default='')
    KY3 = models.CharField(max_length=100, default='')

    class Meta:
        ordering = ('created',)

#股票技术指标数据表
class TechnicalData(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    stockData = models.ForeignKey(StockData, on_delete=models.CASCADE)
    technicalDatas = models.TextField(default='')
    dimension = models.IntegerField(blank=True, null=True)#特征维度
    number = models.IntegerField(blank=True, null=True)
    filePath = models.CharField(max_length=250,default='')
    isExpired = models.BooleanField(default=False)
    note = models.TextField(default='')
    KY1 = models.CharField(max_length=100, default='')#指标数据集名称
    KY2 = models.CharField(max_length=100, default='')
    KY3 = models.CharField(max_length=100, default='')

    class Meta:
        ordering = ('created',)

#选股策略表
class Strategy(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='')#策略名称
    algorithm = models.CharField(max_length=100, default='')#算法名称
    modelPath = models.CharField(max_length=250,default='')#模型路径
    evaResult = models.CharField(max_length=100, blank=True, default='')#评价结果
    dataNote = models.TextField(default='')#训练数据集说明
    inputNote = models.TextField(default='')#输入数据要求
    isExpired = models.BooleanField(default=False)
    note = models.TextField(default='')
    KY1 = models.CharField(max_length=100, default='')
    KY2 = models.CharField(max_length=100, default='')
    KY3 = models.CharField(max_length=100, default='')

    class Meta:
        ordering = ('created',)

#选股策略预测表
class StrategyPre(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=100, default='')#单只股票的代码
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE)#选股策略
    result = models.CharField(max_length=100, blank=True, default='')#单只股票预测结果
    result1 =  models.CharField(max_length=100, blank=True, default='')#财务数据集上涨股票的集合
    result2 = models.CharField(max_length=100, blank=True, default='')#预测的数据集中下跌股票的集合
    result3 = models.CharField(max_length=100, blank=True, default='')#预测的数据集中平稳股票的集合
    isExpired = models.BooleanField(default=False)#过期标志
    note = models.TextField(default='')#备注
    KY1 = models.CharField(max_length=100, default='')#预测名称
    KY2 = models.CharField(max_length=100, default='')#预测的财务数据集
    KY3 = models.CharField(max_length=100, default='')#空余字段

    class Meta:
        ordering = ('created',)

#股票预测算法表
class Algorithm(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='')
    a1 = models.CharField(max_length=100, blank=True, default='')
    a2 = models.CharField(max_length=100, blank=True, default='')
    a3 = models.CharField(max_length=100, blank=True, default='')
    a4 = models.CharField(max_length=100, blank=True, default='')
    a5 = models.CharField(max_length=100, blank=True, default='')
    a6 = models.CharField(max_length=100, blank=True, default='')
    a7 = models.CharField(max_length=100, blank=True, default='')
    a8 = models.CharField(max_length=100, blank=True, default='')
    a9 = models.CharField(max_length=100, blank=True, default='')
    a10 = models.CharField(max_length=100, blank=True, default='')
    isExpired = models.BooleanField(default=False)
    note = models.TextField(default='')

    class Meta:
        ordering = ('created',)

#股票预测模型表
class ModelA(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='')
    algorithm = models.ForeignKey(Algorithm,on_delete=models.CASCADE)
    stockData = models.ForeignKey(StockData,on_delete=models.CASCADE)
    m1 = models.CharField(max_length=100, blank=True, default='')
    m2 = models.CharField(max_length=100, blank=True, default='')
    m3 = models.CharField(max_length=100, blank=True, default='')
    m4 = models.CharField(max_length=100, blank=True, default='')
    m5 = models.CharField(max_length=100, blank=True, default='')
    m6 = models.CharField(max_length=100, blank=True, default='')
    m7 = models.CharField(max_length=100, blank=True, default='')
    m8 = models.CharField(max_length=100, blank=True, default='')
    m9 = models.CharField(max_length=100, blank=True, default='')
    m10 = models.CharField(max_length=100, blank=True, default='')
    isExpired = models.BooleanField(default=False)
    note = models.TextField(default='')
    modelPath = models.CharField(max_length=250,default='')
    result = models.CharField(max_length=100, blank=True, default='')
    r1 = models.CharField(max_length=3000, blank=True, default='')
    r2 = models.CharField(max_length=3000, blank=True, default='')
    r3 = models.CharField(max_length=3000, blank=True, default='')
    r4 = models.CharField(max_length=3000, blank=True, default='')
    r5 = models.CharField(max_length=3000, blank=True, default='')

    class Meta:
        ordering = ('created',)

#股票预测结果表
class ModelPre(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=100, default='')
    modelA = models.ForeignKey(ModelA, on_delete=models.CASCADE)
    m1 = models.CharField(max_length=100, blank=True, default='')
    m2 = models.CharField(max_length=100, blank=True, default='')
    m3 = models.CharField(max_length=100, blank=True, default='')
    m4 = models.CharField(max_length=100, blank=True, default='')
    m5 = models.CharField(max_length=100, blank=True, default='')
    result = models.CharField(max_length=100, blank=True, default='')
    dataStr = models.TextField(default='')#原始收盘价序列和预测的收盘价序列的组合
    result1 = models.CharField(max_length=100, blank=True, default='')
    result2 = models.CharField(max_length=100, blank=True, default='')
    result3 = models.CharField(max_length=100, blank=True, default='')
    isExpired = models.BooleanField(default=False)
    note = models.TextField(default='')
    KY1 = models.CharField(max_length=100, default='')#预测名称
    KY2 = models.CharField(max_length=100, default='')#预测日期
    KY3 = models.CharField(max_length=100, default='')#数据集ID

    class Meta:
        ordering = ('created',)

# the following code write by ln
# 择时策略表
class Choice_t_strategy(models.Model):
    createTime = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='')
    interface = models.CharField(max_length=100, default='')
    # blank=true允许为空
    # path用来存储策略的分类  如：趋势追踪，市场情绪等
    path = models.CharField(max_length=250, default='')
    describe = models.TextField(default='')
    describe_data = models.TextField(default='')
    isExpired = models.BooleanField(default=False)

    class Meta:
        ordering = ('createTime',)
    def __str__(self):
        return "%s" %(self.name)
    @classmethod
    def createCTS(cls, name, interface,path, describe, describe_data):
        cts = cls(name=name, interface=interface, path=path,describe=describe,
                   describe_data=describe_data, createTime=datetime.datetime.now(),
                   isExpired=False)
        return cts

# 选股策略表
class Choice_s_strategy(models.Model):
    createTime = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='')
    interface = models.CharField(max_length=100, default='')
    # blank=true允许为空
    path = models.CharField(max_length=250, default='')
    describe = models.TextField(default='')
    describe_data = models.TextField(default='')
    isExpired = models.BooleanField(default=False)

    class Meta:
        ordering = ('createTime',)
    # def __str__(self):
    #     return "%s-%s" %(self.code, self.name)
    @classmethod
    def createCSS(cls, name, interface,path, describe, describe_data):
        css = cls(name=name, interface=interface, path=path,describe=describe,
                   describe_data=describe_data, createTime=datetime.datetime.now(),
                   isExpired=False)
        return css

# 特征选择方法
class feature_c_method(models.Model):
    createdTime = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='')
    interface = models.CharField(max_length=100, default='')
    # blank=true允许为空
    path = models.CharField(max_length=250, default='')
    describe = models.TextField(default='')
    describe_data = models.TextField(default='')
    isExpired = models.BooleanField(default=False)

    class Meta:
        ordering = ('createdTime',)
    def __str__(self):
        return "%s" %(self.name)
    @classmethod
    def createFCM(cls, name, interface,path, describe, describe_data):
        fcm = cls(name=name, interface=interface, path=path,describe=describe,
                   describe_data=describe_data, createdTime=datetime.datetime.now(),
                   isExpired=False)
        return fcm

# 买卖点检测方法
class bsp_c_method(models.Model):
    createdTime = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='')
    interface = models.CharField(max_length=100, default='')
    # blank=true允许为空
    path = models.CharField(max_length=250, default='')
    describe = models.TextField(default='')
    describe_data = models.TextField(default='')
    isExpired = models.BooleanField(default=False)

    class Meta:
        ordering = ('createdTime',)
    # def __str__(self):
    #     return "%s-%s" %(self.code, self.name)
    @classmethod
    def createBSP(cls, name, interface,path, describe, describe_data):
        bsp = cls(name=name, interface=interface, path=path,describe=describe,
                   describe_data=describe_data, createdTime=datetime.datetime.now(),
                   isExpired=False)
        return bsp

# 趋势识别方法
class trend_c_method(models.Model):
    createdTime = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='')
    interface = models.CharField(max_length=100, default='')
    # blank=true允许为空
    path = models.CharField(max_length=250, default='')
    describe = models.TextField(default='')
    describe_data = models.TextField(default='')
    isExpired = models.BooleanField(default=False)

    class Meta:
        ordering = ('createdTime',)
    # def __str__(self):
    #     return "%s-%s" %(self.code, self.name)
    @classmethod
    def createTCM(cls, name, interface,path, describe, describe_data):
        tcm = cls(name=name, interface=interface, path=path,describe=describe,
                   describe_data=describe_data, createTime=datetime.datetime.now(),
                   isExpired=False)
        return tcm

# 买卖点预测算法
class BSP_Algorithm(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='')
    interface = models.CharField(max_length=100, default='')
    a1 = models.CharField(max_length=100, blank=True, default='')
    a2 = models.CharField(max_length=100, blank=True, default='')
    a3 = models.CharField(max_length=100, blank=True, default='')
    a4 = models.CharField(max_length=100, blank=True, default='')
    a5 = models.CharField(max_length=100, blank=True, default='')
    a6 = models.CharField(max_length=100, blank=True, default='')
    a7 = models.CharField(max_length=100, blank=True, default='')
    a8 = models.CharField(max_length=100, blank=True, default='')
    a9 = models.CharField(max_length=100, blank=True, default='')
    isExpired = models.BooleanField(default=False)
    note = models.TextField(blank=True, default='')

    def __str__(self):
        return "%s" %(self.name)

    class Meta:
        ordering = ('created',)

#买卖点预测模型表
class BSP_Predict_Model(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='')
    algorithm = models.ForeignKey(BSP_Algorithm,on_delete=models.CASCADE)
    bsp_recognize_s = models.ForeignKey(Choice_t_strategy, on_delete=models.CASCADE )
    bsp_recognize = models.ForeignKey(bsp_c_method,on_delete=models.CASCADE )
    f_choice = models.ForeignKey(feature_c_method,on_delete=models.CASCADE )
    tidata = models.ForeignKey(TechnicalData,on_delete=models.CASCADE)
    m1 = models.CharField(max_length=100, blank=True, default='')
    m2 = models.CharField(max_length=100, blank=True, default='')
    m3 = models.CharField(max_length=100, blank=True, default='')
    m4 = models.CharField(max_length=100, blank=True, default='')
    m5 = models.CharField(max_length=100, blank=True, default='')
    m6 = models.CharField(max_length=100, blank=True, default='')
    m7 = models.CharField(max_length=100, blank=True, default='')
    m8 = models.CharField(max_length=100, blank=True, default='')
    m9 = models.CharField(max_length=100, blank=True, default='')
    m10 = models.CharField(max_length=100, blank=True, default='')
    isExpired = models.BooleanField(default=False)
    note = models.TextField(blank=True,default='')
    modelPath = models.CharField(max_length=250,default='')
    # 存储预测结果的地址
    result = models.CharField(max_length=100, blank=True, default='')
    r1 = models.CharField(max_length=300, blank=True, default='')
    r2 = models.CharField(max_length=300, blank=True, default='')
    r3 = models.CharField(max_length=300, blank=True, default='')
    r4 = models.CharField(max_length=300, blank=True, default='')
    r5 = models.CharField(max_length=300, blank=True, default='')

    def __str__(self):
        return "%s" %(self.name)

    class Meta:
        ordering = ('created',)

#买卖点预测结果表
class BSP_Pre_Result(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=100, default='')
    pre_model = models.ForeignKey(BSP_Predict_Model, on_delete=models.CASCADE)
    m1 = models.CharField(max_length=100, blank=True, default='')
    m2 = models.CharField(max_length=100, blank=True, default='')
    m3 = models.CharField(max_length=100, blank=True, default='')
    m4 = models.CharField(max_length=100, blank=True, default='')
    m5 = models.CharField(max_length=100, blank=True, default='')
    result_path = models.CharField(max_length=200, blank=True, default='')
    dataStr = models.TextField(default='')#原始收盘价序列和预测的收盘价序列的组合
    result1 = models.CharField(max_length=100, blank=True, default='')
    result2 = models.CharField(max_length=100, blank=True, default='')
    result3 = models.CharField(max_length=100, blank=True, default='')
    isExpired = models.BooleanField(default=False)
    note = models.TextField(blank=True,default='')
    KY1 = models.CharField(max_length=100, default='')#预测名称
    KY2 = models.CharField(max_length=100, default='')#预测日期
    KY3 = models.CharField(max_length=100, default='')#数据集ID

    def __str__(self):
        return "%s" %(self.KY1)

    class Meta:
        ordering = ('created',)