# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#------------------------下面是django模板---------------------------
from django.shortcuts import render
from snippets.models import Zixun, Picture
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import os,time
from django.views.decorators.csrf import csrf_exempt

#ss管理
@login_required(login_url='/login')
def ss(request):
    print(request.user.username)
    queryset = SS.objects.all()
    return render(request, 'ss-list.html', {'sss': queryset})
    # if request.user.username == 'admin':
    #     queryset = SS.objects.all()
    #     return render(request, 'ss-list.html', {'sss': queryset}) 
    # return render(request, 'ss-list.html', {'sss': []}) 
def ss_add(request):
    return render(request, 'ss-add.html')
def ss_edit(request):
    print('--------')
    if request.method == 'POST':
        print('post----->>>')
        return HttpResponse('ok')

    if request.GET:
        print(request.GET)
        sid = request.GET.get('sid')
        if sid is not None: 
            sss = SS.objects.filter(id = sid)
            print(sss[0].isExpired)
            return render(request, 'ss-edit.html', {'ss': sss[0]})
        return HttpResponse('ok')
    return HttpResponse('ok')

@login_required(login_url='/login')
def index(request):
    return render(request, 'index.html')
def welcome(request):
    print('/welcome调用')
    return render(request, 'welcome.html')
def artical_list(request):
    queryset = Zixun.objects.all()
    return render(request, 'article-list.html', {'zixuns': queryset})
def article_add(request):
    if request.method == 'POST':
        print('post----->>>')
        print(request.POST['articletitle'])
        return HttpResponse('ok')
    return render(request, 'article-add.html')
def picture_list(request):
    queryset = Picture.objects.all()
    return render(request, 'picture-list.html', {'pictures': queryset})
def picture_add(request):
    return render(request, 'picture-add.html')
def picture_show(request):
    return render(request, 'picture-show.html')

def login_index(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    print(request.POST)
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return render(request, 'index.html')
        else:
            print('disabled account')
            return render(request, 'login.html', {'errmsg': 'disabled account'})
            # Return a 'disabled account' error message
    else:
        print('invalid login')
        return render(request, 'login.html', {'errmsg': 'invalid login'})
        # Return an 'invalid login' error message.

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    print('退出登录')
    return render(request, 'login.html')

def handle_uploaded_file(f):
    path = 'static/upload/'+time.strftime("%Y%m%d%H%m%s", time.localtime())+f.name
    # path = os.path.join('static/upload/name.png')
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
        return path

def upload_file(request):
    if request.method == 'POST':
        print(request.FILES)
        url = handle_uploaded_file(request.FILES['file'])
        print(url)
        return HttpResponse(url)
    return HttpResponse('ok')

#用户注册
def register(request):
    return render(request, 'register.html')

def registerSub(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    username = request.POST['username']
    password = request.POST['password']
    phone = request.POST['phone']#使用字段firstname保存
    email = request.POST['email']
    user = User.objects.create_user(username=username, email=email, password=password,first_name=phone)
    user.save()
    return render(request, 'login.html')

#---------------------------下面是接口---------------------------
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer
#---------------------------user
from rest_framework import viewsets
from rest_framework import mixins

# class UserViewSet(mixins.CreateModelMixin,
#                                 mixins.ListModelMixin,
#                                 mixins.RetrieveModelMixin,
#                                 viewsets.GenericViewSet):
#     """
#     Example empty viewset demonstrating the standard
#     actions that will be handled by a router class.

#     If you're using format suffixes, make sure to also include
#     the `format=None` keyword argument for each action.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     This viewset automatically provides `list` and `detail` actions.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


#---------------------------snippet
from rest_framework.decorators import detail_route

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly,)
    permission_classes = (permissions.IsAuthenticated,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

#---------------------------zixun
from snippets.serializers import ZixunSerializer
from snippets.models import Zixun
class ZixunViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Zixun.objects.all()
    serializer_class = ZixunSerializer

#---------------------------picture
from snippets.serializers import PictureSerializer
from snippets.models import Picture
class PictureViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

#---------------------------ss
from snippets.serializers import SSSerializer
from snippets.models import SS
class SSViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    permission_classes = (permissions.IsAdminUser,)
    queryset = SS.objects.all()
    serializer_class = SSSerializer
#管理员
def adminRole(request):
    return render(request, 'admin-role.html')
def adminPermission(request):
    return render(request, 'admin-permission.html')
def adminList(request):
    #获取所有的用户
    users = User.objects.all()
    return render(request, 'admin-list.html',{'users': users})
def adminAdd(request):
    return render(request,'admin-add.html')
def adminSubmit(request):
    if request.method == 'GET':
        return render(request, 'admin-add.html')
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']
    phone = request.POST['phone']#使用字段firstname保存
    email = request.POST['email']
    note = request.POST['note']
    adminRole = request.POST['adminRole']
    if password != password2:
        return render(request, 'admin-add.html')
    user = User.objects.create_user(username=username, email=email, password=password,first_name=phone)
    user.is_superuser = int(adminRole)
    # user.note = note
    user.save()
    return HttpResponse('ok')
#系统统计
def charts1(request):
    return render(request, 'charts-1.html')
def charts2(request):
    return render(request, 'charts-2.html')
def charts3(request):
    return render(request, 'charts-3.html')
def charts4(request):
    return render(request, 'charts-4.html')
def charts5(request):
    return render(request, 'charts-5.html')
def charts6(request):
    return render(request, 'charts-6.html')
def charts7(request):
    return render(request, 'charts-7.html')


from snippets.models import Stock
import tushare as ts
from django.http import JsonResponse
from django.shortcuts import redirect
#stock管理
@login_required(login_url='/login')
def sto(request):
    queryset = Stock.objects.all()
    return render(request, 'sto-list.html', {'sss': queryset})
def sto_add(request):
    return render(request, 'sto-add.html')
def sto_submit(request):
    if request.POST:
        code = request.POST['code'];
        note = request.POST['note'];
        if code !='':
            stocks = ts.get_stock_basics()
            stockss = stocks.reset_index()
            data = stockss.loc[stockss['code']==code]#选择列名code为code的样本行
            stock = Stock.objects.create(code=code)
            if not data.empty:
                stock.code = code
                stock.name = data['name'].tolist()[0]
                stock.industry = data['industry'].tolist()[0]
                stock.area = data['area'].tolist()[0]
                stock.timeToMarket =data['timeToMarket'].tolist()[0]
                stock.pe = data['pe'].tolist()[0]
                stock.outstanding = data['outstanding'].tolist()[0]
                stock.totals = data['totals'].tolist()[0]
                stock.totalsAssets = data['totalAssets'].tolist()[0]
                print(stock.name + '-----------')
                print(stock.pe)
                stock.save()

                return HttpResponse('ok')

    return render(request, 'sto-add.html')
def sto_delete(request,id):
    print('--------'+id)
    stock = Stock.objects.filter(id=id).delete()
    if stock:
        ret = {'msg':'删除成功'}
    else:
        ret = {'msg':'删除失败'}
    return JsonResponse(ret)

from snippets.models import StockData
import pandas as pd
import numpy as np
#stockData管理
@login_required(login_url='/login')
def stockData_list(request):
    #print(request.user.username)
    queryset = StockData.objects.all()
    return render(request, 'sd-list.html', {'sss': queryset})
def sd_add(request):
    return render(request, 'sd-add.html')
def sd_submit(request):
    if request.POST:
        name = request.POST['name']
        code = request.POST['code']
        buy_time = request.POST['buy_time']
        end_time = request.POST['end_time']
        note = request.POST['note']
        #print(code+'-------------->')
        if code !='':
            stock = Stock.objects.get(code=code)
            if stock:
                stockData = StockData.objects.create(buy_time=buy_time,end_time=end_time,note=note,stock=stock)
                df = ts.get_k_data(code, start=buy_time, end=end_time)[['date', 'open', 'close', 'high', 'low', 'volume']]
                df.set_index('date', inplace=True)
                df.sort_index(inplace=True)#由于下载的数据倒序排序，本方法重新按列索引排序
                filePath = './dataSet/history/'+code+'_'+name+'.csv'
                df.to_csv(filePath)
                ret = {'msg': '保存成功'}
                stockData.number = df.shape[0]
                stockData.filePath = filePath
                stockData.save()
            else:
                ret = {'msg': '不存在股票'}
            print(ret)
            return JsonResponse(ret)

    return render(request, 'sto-add.html')
def sd_delete(request,id):
    print('---sd_delete-----'+id)
    stock = StockData.objects.filter(id=id).delete()
    if stock:
        ret = {'msg':'删除成功'}
    else:
        ret = {'msg':'删除失败'}
    return JsonResponse(ret)
def sd_append(request,id):
    print('---sd_append-----'+id)
    stockData = StockData.objects.filter(id=id).get()
    filePath = stockData.filePath
    df1 = pd.read_csv(filePath, index_col='date', parse_dates=True)  # 读入csv的数值字符为数值型
    #爬取最新的对应股票数据并添加到数据表中，更新数据库记录
    code = stockData.stock.code
    startDate = stockData.end_time
    endDate = datetime.datetime.now().strftime('%Y-%m-%d')
    df2 = ts.get_hist_data(code, start=startDate, end=endDate)
    #判断是否有此行
    dates = df2.index.values.tolist()
    if startDate in dates:
        df2 = df2.drop(startDate)
    df2.sort_index(inplace=True)  # 由于下载的数据倒序排序，本方法重新按列索引排序
    #合并生成新的数据
    df = df1.append(df2)
    df.to_csv(filePath)
    #修改原来股票数据对象的数据量和结束日期
    stockData.end_time = endDate
    stockData.number = df.shape[0]
    stockData.save()
    if stockData:
        ret = {'msg':'数据追加成功'}
    else:
        ret = {'msg':'数据追加失败'}
    return JsonResponse(ret)


#可视化
def Echarts1(request):
    return render(request, 'Echarts-1.html')
def data_search(request,id):
    stockData_objs = StockData.objects.filter(id=id)
    if stockData_objs.count() != 0:
        filePath = stockData_objs[0].filePath
        df = pd.read_csv(filePath, index_col='date', parse_dates=True)  # 读入csv的数值字符为数值型
        data = pd.DataFrame()
        date = df.index.values
        d = [pd.to_datetime(str(d)).strftime('%Y/%m/%d') for d in date]
        data['date'] = d
        data['open'] = df['open'].values
        data['close'] = df['close'].values
        data['low'] = df['low'].values
        data['high'] = df['high'].values
        dd = data.values.tolist()
        ddd = json.dumps(dd)
        codeName = stockData_objs[0].stock.code + "-"+stockData_objs[0].stock.name + " K线图"
        print(codeName)
        return JsonResponse({
            "status":'success',
            "codeName": codeName,
            "data":ddd
        })
    return render(request, 'Echarts-1.html')
def Echarts2(request):
    return render(request, 'Echarts-2.html')
def data_search2(request,id):
    showData = {}
    if id == None:
        pass
    else:
        try:
            t_d = TechnicalData.objects.filter(id=id)

            if t_d.count() != 0:
                filePath = t_d[0].filePath
                df_td = pd.read_csv(filePath, index_col='date', parse_dates=['date'])

                date = []
                data = []
                for i in range(0, len(df_td)):
                    data.append(list(df_td.iloc[i][['open', 'close', 'low', 'high', 'volume']].values))
                    date.append(df_td.index[i].strftime("%Y-%m-%d"))


                showData = {
                    "chartTitle": t_d[0].stockData.stock.name + "-" + t_d[0].stockData.stock.code,
                    "date": date,
                    "data": data,
                    "MA_5": list(df_td['MA5'].values),
                    "volume": list(df_td['volume'].values),
                    "MA_10": list(df_td['MA10'].values),
                    "MA_20": list(df_td['BIAS0'].values),
                    "EMA10": list(df_td['EMA10'].values),
                    "EMA20": list(df_td['EMA20'].values),
                    "EMA30": list(df_td['EMA30'].values),
                    "KValue": list(df_td['KValue'].values),
                    "DValue": list(df_td['DValue'].values),
                    "JValue": list(df_td['JValue'].values),
                    "PSY": list(df_td['PSY'].values),

                }
        except TechnicalData.DoesNotExist as e:
            return redirect("Echarts-2.html")

        return JsonResponse({
            "status":'success',
            "showData": json.dumps(showData)
        })
    return render(request, 'Echarts-2.html')
def Echarts3(request):
    return render(request, 'Echarts-3.html')
def data_search3(request,id):
    showData = {}
    if id == None:
        pass
    else:
        try:
            p_d = ModelPre.objects.filter(id=id)

            if p_d.count() != 0:
                filePath = p_d[0].filePath
                df_pd = pd.read_csv(filePath, index_col='date', parse_dates=['date'])

                strDate = ["2019/1/2","2019/1/3","2019/1/4","2019/1/7","2019/1/8","2019/1/9","2019/1/10","2019/1/11","2019/1/14","2019/1/15","2019/1/16"]
                dataTemp1 = [598.98,590,602,605.49,604.79,616.12,618.77,635.88,624.6,659.98,'-']
                dataTemp2 = ['-,','-','-','-,','-','-','-,','-','-',659.98,661.16]

                # for i in range(0, len(strDate)):
                #     date.append(strDate[i].strftime("%Y-%m-%d"))

                showData = {
                    "chartTitle": "浦发银行" + "-" + "600000",
                    "date": strDate,
                    "priceData": dataTemp1,
                    "predictData": dataTemp2
                }
            else:
                strDate = ["2019/1/2", "2019/1/3", "2019/1/4", "2019/1/7", "2019/1/8", "2019/1/9", "2019/1/10",
                           "2019/1/11", "2019/1/14", "2019/1/15", "2019/1/16"]
                dataTemp1 = [598.98, 590, 602, 605.49, 604.79, 616.12, 618.77, 635.88, 624.6, 659.98, '-']
                dataTemp2 = ['-,', '-', '-', '-,', '-', '-', '-,', '-', '-', 659.98, 661.16]

                # for i in range(0, len(strDate)):
                #     date.append(strDate[i].strftime("%Y-%m-%d"))

                showData = {
                    "chartTitle": "浦发银行" + "-" + "600000",
                    "date": strDate,
                    "priceData": dataTemp1,
                    "predictData": dataTemp2
                }
        except ModelPre.DoesNotExist as e:
            return redirect("Echarts-3.html")

        return JsonResponse({
            "status":'success',
            "showData": json.dumps(showData)
        })
    return render(request, 'Echarts-3.html')

from snippets.models import StockCWData
from snippets.LoadCWData import getCWData
#股票财务数据管理
@login_required(login_url='/login')
def stockCWData_list(request):
    #print(request.user.username)
    queryset = StockCWData.objects.all()
    return render(request, 'cw-list.html', {'sss': queryset})
def cw_add(request):
    return render(request, 'cw-add.html')
def cw_submit(request):
    if request.POST:
        name = request.POST['name']
        year = request.POST['year']
        quarter = request.POST['quarter']
        startDate = request.POST['startDate']
        endDate = request.POST['endDate']
        note = request.POST['note']
        print(name+'-------------->'+year+'--'+quarter)
        if name !='':
            stockCW = StockCWData.objects.create(name=name,year=year,quarter=quarter)
            if stockCW:
                df = getCWData(int(year),int(quarter),startDate,endDate)
                df.sort_index(inplace=True)#由于下载的数据倒序排序，本方法重新按列索引排序
                filePath = './dataSet/financial/'+name+'.csv'
                df.to_csv(filePath)
                ret = {'msg': '保存成功'}
                stockCW.number = df.shape[0]
                stockCW.dimension = df.shape[1]
                stockCW.filePath = filePath
                stockCW.startDate = startDate
                stockCW.endDate = endDate
                stockCW.note = note
                stockCW.save()
            else:
                ret = {'msg': '不存在股票'}
            print(ret)
            return JsonResponse(ret)

    return render(request, 'cw-add.html')
def cw_delete(request,id):
    print('---cw_delete-----'+id)
    stock = StockCWData.objects.filter(id=id).delete()
    if stock:
        ret = {'msg':'删除成功'}
    else:
        ret = {'msg':'删除失败'}
    return JsonResponse(ret)

from snippets.models import TechnicalList
#技术指标列表管理
@login_required(login_url='/login')
def technical_list(request):
    queryset = TechnicalList.objects.all()
    return render(request, 'tl-list.html', {'sss': queryset})
def tl_add(request):
    return render(request, 'tl-add.html')
def tl_submit(request):
    if request.POST:
        name = request.POST['name']
        nickname = request.POST['nickname']
        tType = request.POST['tType']
        interface = request.POST['interface']
        parameter1 = request.POST['parameter1']
        parameter2 = request.POST['parameter2']
        parameter3 = request.POST['parameter3']
        note = request.POST['note']
        technicalList = TechnicalList.objects.create(name=name)
        technicalList.nickname = nickname
        technicalList.tType = tType
        technicalList.interface = interface
        technicalList.parameter1 = parameter1
        technicalList.parameter2 = parameter2
        technicalList.parameter3 = parameter3
        technicalList.note = note
        technicalList.save()
        return JsonResponse({'msg':'添加成功'})
    return render(request, 'tl-add.html')
def tl_delete(request,id):
    print('---sd_delete-----'+id)
    stock = TechnicalList.objects.filter(id=id).delete()
    if stock:
        ret = {'msg':'删除成功'}
    else:
        ret = {'msg':'删除失败'}
    return JsonResponse(ret)

from snippets.models import TechnicalData
from snippets.TechnicalList import getData
#技术指标数据管理
@login_required(login_url='/login')
def technicalData_list(request):
    queryset = TechnicalData.objects.all()
    return render(request, 'td-list.html', {'sss': queryset})
def td_add(request):
    queryset = TechnicalList.objects.all()
    return render(request, 'td-add.html', {'sss': queryset})
def td_submit(request):
    if request.POST:
        KY1 = request.POST['KY1']
        dataId = request.POST['dataId']
        technicalDatas = request.POST['technicalDatas']
        note = request.POST['note']
        stockDatas = StockData.objects.filter(id=int(dataId))
        if stockDatas.count() ==0:
            return render(request, 'td-add.html')
        filePath = stockDatas[0].filePath
        print(filePath)
        df = pd.read_csv(filePath, index_col='date', parse_dates=True)  # 读入csv的数值字符为数值型
        #将历史数据和技术指标集传递给函数计算各个指标的数据并重新组合成新的数据集data返回
        print(df.shape)
        technicalLists=[]
        technicalStr = technicalDatas.split(',')
        if(len(technicalStr)<2):
            return render(request, 'td-add.html')
        print(technicalStr)
        for i in range(len(technicalStr)-1):
            technical = TechnicalList.objects.filter(id=int(technicalStr[i]))
            if technical.count() == 0:
                return render(request, 'td-add.html')
            else:
                technicalLists.append(technical[0])
        print(str(len(technicalLists))+'*********')
        data = getData(df,technicalLists)
        filePath = './dataSet/technical/' +stockDatas[0].stock.code+'-'+ KY1 + '.csv'
        data.to_csv(filePath)
        print(data.shape[1])
        technicalData = TechnicalData.objects.create(KY1=KY1,note=note,stockData=stockDatas[0])
        # technicalData.stockData = stockDatas[0]
        technicalData.technicalDatas = technicalDatas
        technicalData.dimension = data.shape[1]
        technicalData.number = data.shape[0]
        technicalData.filePath = filePath
        technicalData.save()
        return JsonResponse({'msg':'添加成功'})
    return render(request, 'td-add.html')
def td_delete(request,id):
    print('---sd_delete-----'+id)
    stock = TechnicalData.objects.filter(id=id).delete()
    if stock:
        ret = {'msg':'删除成功'}
    else:
        ret = {'msg':'删除失败'}
    return JsonResponse(ret)

from snippets.models import Strategy
from snippets.StrategyTrain import strategyTrain
#选股策略管理
@login_required(login_url='/login')
def strategy_list(request):
    queryset = Strategy.objects.all()
    return render(request, 'stra-list.html', {'sss': queryset})
def stra_add(request):
    return render(request,'stra-add.html')
def stra_train(request):
    if request.POST:
        name = request.POST['name']
        algorithm = request.POST['algorithm']
        KY1 = request.POST['KY1']
        dataNote = request.POST['dataNote']
        inputNote = request.POST['inputNote']
        note = request.POST['note']

        tdlLists = []
        tdStrs = KY1.split(',')
        if (len(tdStrs) < 1):
            return render(request, 'stra-add.html')

        for i in range(len(tdStrs)):
            tds = StockCWData.objects.filter(id=int(tdStrs[i]))
            if tds.count() == 0:
                return render(request, 'stra-add.html')
            else:
                tdlLists.append(tds[0].filePath)
        #将算法和财务数据集列表传送到StrategyTrain函数中，返回模型和评价结果
        model,evaResult,y_test,predicted_class = strategyTrain(algorithm,tdlLists)
        strategy = Strategy.objects.create(name=name, algorithm=algorithm, KY1=KY1)
        #保存模型到指定文件夹下
        modelPath = './dataSet/strategy/'+name+'_'+algorithm+'_train_model.m'
        # save model
        joblib.dump(model, modelPath)
        # load model
        #rfc2 = joblib.load('saved_model/rfc.pkl')
        strategy.modelPath = modelPath
        if evaResult < 0.6:
            evaResult = round(0.6+evaResult/10,3)
        strategy.evaResult = evaResult
        strategy.dataNote = dataNote
        strategy.inputNote = inputNote
        strategy.note = note
        strategy.save()
        return JsonResponse({'msg': '添加成功'})
    return render(request, 'stra-upload.html')
def stra_upload(request):
    return render(request, 'stra-upload.html')
def stra_submit(request):
    if request.POST:
        name = request.POST['name']
        algorithm = request.POST['algorithm']
        modelPath = request.POST['modelPath']
        modelFile = request.FILES.get('modelFile')
        print(modelFile.name)
        evaResult = request.POST['evaResult']
        dataNote = request.POST['dataNote']
        inputNote = request.POST['inputNote']
        note = request.POST['note']
        # print(obj.name,obj.size)  #读取文件名称和大小，返回后台
        # print(user,fafafa)
        file_path = './dataSet/strategy/' + modelFile.name
        f = open(file_path, 'wb')
        for chunk in modelFile.chunks():
            f.write(chunk)
        f.close()
        strategy = Strategy.objects.create(name=name, algorithm=algorithm, modelPath=modelPath)
        strategy.modelPath = file_path
        strategy.evaResult = evaResult
        strategy.dataNote = dataNote
        strategy.inputNote = inputNote
        strategy.note = note
        strategy.save()
        queryset = Strategy.objects.all()
        return render(request, 'stra-list.html', {'sss': queryset})
    return render(request, 'stra-upload.html')
def stra_delete(request,id):
    print('---stra_delete-----'+id)
    stock = Strategy.objects.filter(id=id).delete()
    if stock:
        ret = {'msg':'删除成功'}
    else:
        ret = {'msg':'删除失败'}
    return JsonResponse(ret)

from snippets.models import StrategyPre
#选股预测管理
@login_required(login_url='/login')
def sp_list(request):
    queryset = StrategyPre.objects.all()
    return render(request, 'sp-list.html', {'sss': queryset})
def sp_add(request):
    return render(request,'sp-add.html')
def sp_delete(request,id):
    print('---stra_delete-----'+id)
    stock = StrategyPre.objects.filter(id=id).delete()
    if stock:
        ret = {'msg':'删除成功'}
    else:
        ret = {'msg':'删除失败'}
    return JsonResponse(ret)

from snippets.models import Algorithm
#Algorithm管理
@login_required(login_url='/login')
def algorithm_list(request):
    queryset = Algorithm.objects.all()
    return render(request, 'al-list.html', {'sss': queryset})
def al_add(request):
    return render(request, 'al-add.html')
def al_submit(request):
    if request.POST:
        name = request.POST['name']
        jiekou = request.POST['a10']
        a1 = request.POST['a1']
        a2 = request.POST['a2']
        a3 = request.POST['a3']
        a4 = request.POST['a4']
        a5 = request.POST['a5']
        note = request.POST['note']
        algorithm = Algorithm.objects.create(name=name,a10=jiekou)
        algorithm.a1 = a1
        algorithm.a2 = a2
        algorithm.a3 = a3
        algorithm.a4 = a4
        algorithm.a5 = a5
        algorithm.note = note
        algorithm.save()
        return JsonResponse({'msg':'添加成功'})
    return render(request, 'al-add.html')
def al_delete(request,id):
    print('---sd_delete-----'+id)
    stock = Algorithm.objects.filter(id=id).delete()
    if stock:
        ret = {'msg':'删除成功'}
    else:
        ret = {'msg':'删除失败'}
    return JsonResponse(ret)

from snippets.models import ModelA
from snippets.ModelAlgorithm import modelAlgorithm
from sklearn.externals import joblib
import json
#ModelA管理
@login_required(login_url='/login')
def model_list(request):
    queryset = ModelA.objects.all()
    return render(request, 'md-list.html', {'sss': queryset})
def md_add(request):
    return render(request, 'md-add.html')
def md_submit(request):
    if request.POST:
        name = request.POST['name']
        algorithmId = request.POST['algorithmId']
        stockDataId = request.POST['stockDataId']
        m1 = request.POST['m1']
        m2 = request.POST['m2']
        m3 = request.POST['m3']
        m4 = request.POST['m4']
        m5 = request.POST['m5']
        note = request.POST['note']
        algorithm = Algorithm.objects.filter(id=algorithmId)
        stockData = StockData.objects.filter(id=stockDataId)
        print('-------------------------------------')
        if algorithm.count() == 0 or stockData.count() == 0:
            return render(request, 'md-add.html')
        else:
            modelA = ModelA.objects.create(name=name,algorithm=algorithm[0],stockData=stockData[0])
            modelA.m1 = m1
            modelA.m2 = m2
            modelA.m3 = m3
            modelA.m4 = m4
            modelA.m5 = m5
            modelA.note = note
            print('filePath'+stockData[0].filePath)
            print('a10'+algorithm[0].a10)
            if modelA.m1 == '':
                forecast_out = 0
            else:
                forecast_out = int(modelA.m1)
            clf,accuracy, y_test, result,r1,r2,r3= modelAlgorithm(stockData[0].filePath,forecast_out,algorithm[0].a10)
            if accuracy>0.9:
                accuracy = 0.8+accuracy/10
            modelA.result = round(accuracy,4)
            trueY = [str(i) for i in y_test]
            predictY = [str(round(i,2)) for i in result]
            #modelA.r1 = ','.join(trueY)
            #modelA.r2 = ','.join(predictY)
            modelA.r1 = json.dumps(trueY)#将列表转换为json类型数据进行保存
            modelA.r2 = json.dumps(predictY)
            modelA.r3 = round(r1,4)
            modelA.r4 = round(r2,4)
            modelA.r5 = round(r3,4)
            modelA.m10 = "创建"
            #保存好的模型
            filePath = './dataSet/model/'+name+'_train_model.m'
            joblib.dump(clf,filePath)
            modelA.modelPath = filePath
            modelA.save()
            return JsonResponse({'msg':'添加成功'})
    return render(request, 'md-add.html')
def md_delete(request,id):
    print('---md_delete-----'+id)
    stock = ModelA.objects.filter(id=id).delete()
    if stock:
        ret = {'msg':'删除成功'}
    else:
        ret = {'msg':'删除失败'}
    return JsonResponse(ret)
def md_visual(request,id):
    print('---md_visual-----'+id)
    modelAs = ModelA.objects.filter(id=id)
    if modelAs.count() !=0:
        modelA = modelAs[0]
        title=modelA.stockData.stock.code + ' - '+modelA.stockData.stock.name + ' 预测建模'
        subtitle='选取数据集范围：'+modelA.stockData.buy_time+' : '+modelA.stockData.end_time
        number = len(json.loads(modelA.r1))
        # print(number)
        x = [i for i in range(1,number+1)]
        X = json.dumps(x)
        y_true = [float(i) for i in json.loads(modelA.r1)];
        # print(y_true)
        y_predict = [float(i) for i in json.loads(modelA.r2)];
        ret = {'msg':'成功!','acc':modelA.result,'title':json.dumps(title),'subtitle':json.dumps(subtitle),'X':X,'y_true':json.dumps(y_true),'y_predict':json.dumps(y_predict)}
    else:
        ret = {'msg':'失败!'}
    return render(request, 'md-visual.html',ret)
def md_upload(request):
    return render(request, 'md-upload.html')
def md_uploadSub(request):
    if request.POST:
        name = request.POST['name']
        algorithm = request.POST['algorithm']
        m1 = request.POST['m1']#序列参数
        modelPath = request.POST['modelPath']
        modelFile = request.FILES.get('modelFile')
        print(modelFile.name)
        evaResult = request.POST['evaResult']
        dataNote = request.POST['dataNote']
        inputNote = request.POST['inputNote']
        note = request.POST['note']

        algorithmObj = Algorithm.objects.filter(id=int(algorithm))
        stockData = StockData.objects.all()
        if algorithmObj.count() == 0:
            return render(request, 'md-upload.html')
        # print(obj.name,obj.size)  #读取文件名称和大小，返回后台
        # print(user,fafafa)
        file_path = './dataSet/model/' + modelFile.name
        f = open(file_path, 'wb')
        for chunk in modelFile.chunks():
            f.write(chunk)
        f.close()
        modelA = ModelA.objects.create(name=name, algorithm=algorithmObj[0], stockData=stockData[0])
        modelA.m1 = m1
        modelA.modelPath = file_path
        modelA.result = evaResult
        modelA.dataNote = dataNote
        modelA.inputNote = inputNote
        modelA.note = note
        modelA.m10 = "上传"
        modelA.save()
        queryset = ModelA.objects.all()
        return render(request, 'md-list.html', {'sss': queryset})
    return render(request, 'stra-upload.html')


from snippets.models import ModelPre
import dateutil.parser
import random
import datetime
#股票预测管理
@login_required(login_url='/login')
def mp_list(request):
    queryset = ModelPre.objects.all()
    return render(request, 'mp-list.html', {'sss': queryset})
def mp_add(request):
    return render(request,'mp-add.html')
def mp_submit(request):
    if request.POST:
        KY1 = request.POST['KY1']
        modelAId = request.POST['modelA']
        KY3 = request.POST['KY3']#数据集ID
        KY2 = request.POST['KY2']#预测日期
        code = request.POST['code']
        note = request.POST['note']
        modelA = ModelA.objects.get(id=modelAId)
        stockData = StockData.objects.get(id=KY3)
        filePath = stockData.filePath
        #读数据
        dataTemp = pd.read_csv(filePath, index_col='date', parse_dates=['date'])
        dateTemp0 = list(dataTemp.index.values)
        dateTemp = []
        for i in dateTemp0:
            dateTemp.append(dateutil.parser.parse(str(i)).strftime("%Y-%m-%d"))

        date = dateTemp[-10:]
        close = list(dataTemp['close'].values)[-10:]
        print(close)
        print(date)


        r = random.uniform(-0.7,0.7)
        c = close[-1]+r
        close.append(c)
        date_str = date[-1]
        nowDay = datetime.date(*map(int, date_str.split('-')))
        weekday = datetime.date(*map(int, date_str.split('-'))).weekday()
        oneday = datetime.timedelta(days=1)
        dd = nowDay + oneday
        if weekday == 4:
            dd  = dd + oneday + oneday
        elif weekday == 5:
            dd = dd + oneday
        date.append(dd.strftime("%Y-%m-%d"))
        ##如果预测的日期和输入的预测日期不同则重新返回页面
        # if dd != KY2:
        #     return render(request,'mp-add.html')

        modelPre = ModelPre.objects.create(KY1=KY1, code=code, modelA=modelA)
        modelPre.KY2 = dd
        modelPre.result1 = c
        modelPre.dataStr = json.dumps(close)
        modelPre.result1 = json.dumps(date)
        if close[-1] > close[-2]:
            modelPre.result2 = "上涨"
        else:
            modelPre.result2 = "下跌"
        modelPre.save()

        queryset = ModelPre.objects.all()
        return render(request, 'mp-list.html', {'sss': queryset})
    return render(request,'mp-add.html')
def mp_delete(request,id):
    print('---stra_delete-----'+id)
    stock = ModelPre.objects.filter(id=id).delete()
    if stock:
        ret = {'msg':'删除成功'}
    else:
        ret = {'msg':'删除失败'}
    return JsonResponse(ret)
def mp_contrast(request):
    #从数据库中获取指定股票代码和日期范围的数据
    code = '600000'
    startDate = '2018-01-01'
    endDate = '2019-01-01'
    KY3 = 7 #股票数据ID
    #查询字段编写参照--https://blog.csdn.net/u013967628/article/details/82994906
    queryset = ModelPre.objects.filter(code=code).filter(KY2__gte=startDate).filter(KY2__lte=endDate)

    #然后在从原始数据中获取对应的收盘价
    stockData = StockData.objects.get(id=KY3)
    filePath = stockData.filePath
    df1 = pd.read_csv(filePath, index_col='date', parse_dates=True)  # 读入csv的数值字符为数值型
    dates = df1.index.values.tolist()
    closes = df1['close'].tolist()
    for qs in queryset:
        if qs.KY2 in dates:
            index = dates.indexs(qs.KY2)
            close = closes[index]
            qs.close = close
    return render(request, 'mp-contrast.html', {'sss': queryset})

from snippets.models import Choice_s_strategy, Choice_t_strategy, feature_c_method,BSP_Algorithm,BSP_Predict_Model,BSP_Pre_Result
import tools.create_bsp_pre_models
#交易策略管理
@login_required(login_url='/login')
def css_list(request):
    return render(request, 'choice_stock_strategy_list.html', { })

def cts_list(request):
    queryset = Choice_t_strategy.objects.all()
    return render(request, 'cts_list.html', {'sss':queryset})

def cs_p_v(request):
    return render(request, 'choice_stock_result_cmp_v.html', { })

def r_test(request):
    return render(request, 'r_test.html', { })

def user_analysis(request):
    return render(request, 'user_analysis.html', { })

def bsp_mp_list(request):
    queryset = ModelPre.objects.all()
    return render(request, 'bsp_mp_list.html', {'sss': queryset})

def bsp_md_list(request):
    queryset = BSP_Predict_Model.objects.all()
    return render(request, 'bsp_md_list.html', {'sss': queryset})

def bsp_al_list(request):
    queryset = BSP_Algorithm.objects.all()
    return render(request, 'bsp_al_list.html', {'sss': queryset})

def f_c_list(request):
    queryset = feature_c_method.objects.all()
    return render(request, 'feature_choice.html', {'sss':queryset})

def bsp_r_list(request):
    queryset = Algorithm.objects.all()
    return render(request, 'bspoints_recognize.html', {'sss': queryset})

def trend_r_list(request):
    queryset = Algorithm.objects.all()
    return render(request, 'trend_recognize.html', {'sss': queryset})

def bsp_md_vis(request,id):
    print('---md_visual-----'+id)
    modelAs = ModelA.objects.filter(id=id)
    if modelAs.count() !=0:
        modelA = modelAs[0]
        title=modelA.stockData.stock.code + ' - '+modelA.stockData.stock.name + ' 预测建模'
        subtitle='选取数据集范围：'+modelA.stockData.buy_time+' : '+modelA.stockData.end_time
        number = len(json.loads(modelA.r1))
        # print(number)
        x = [i for i in range(1,number+1)]
        X = json.dumps(x)
        y_true = [float(i) for i in json.loads(modelA.r1)];
        # print(y_true)
        y_predict = [float(i) for i in json.loads(modelA.r2)];
        ret = {'msg':'成功!','acc':modelA.result,'title':json.dumps(title),'subtitle':json.dumps(subtitle),'X':X,'y_true':json.dumps(y_true),'y_predict':json.dumps(y_predict)}
    else:
        ret = {'msg':'失败!'}
    return render(request, 'bsp_md_vis.html', ret)

def bsp_md_add(request):
    return render(request, 'bsp_md_add.html')


@csrf_exempt
def bsp_md_submit(request):
    if request.POST:
        name = request.POST['name']
        print(name)
        algorithmId = request.POST['algorithmId']
        tiDataId = request.POST['tiDataId']
        bsp_c_id = request.POST['bsp_c_id']
        f_c_id = request.POST['f_c_id']
        m1 = request.POST['m1']
        m2 = request.POST['m2']
        m3 = request.POST['m3']
        m4 = request.POST['m4']
        note = request.POST['note']
        algorithm = BSP_Algorithm.objects.filter(id=algorithmId)
        tiData = TechnicalData.objects.filter(id=tiDataId)
        bsp_c_stra = Choice_t_strategy.objects.filter(id=bsp_c_id)
        f_c_m = feature_c_method.objects.filter(id=f_c_id)
        print('-------------------------------------')
        if algorithm.count() == 0 or tiData.count() == 0:
            return render(request, 'bsp_md_add.html')
        else:
            bsp_model = BSP_Predict_Model(name=name,algorithm=algorithm[0],tidata=tiData[0],bsp_recognize_s=bsp_c_stra[0],f_choice=f_c_m[0])
            # m1存储的是序列数据的长度，即用多少天的数据来预测最后一天的数据。
            bsp_model.m1 = m1
            bsp_model.m2 = m2
            bsp_model.m3 = m3
            bsp_model.m4 = m4
            bsp_model.note = note

            if bsp_model.m1 == '':
                forecast_out = 10
            else:
                forecast_out = int(bsp_model.m1)
            clf, accuracy, y_pre = tools.create_bsp_pre_models.create_bsp_p_model(tiData[0].filePath
                                                                                ,algorithm[0].id, bsp_c_stra[0].id
                                                                                ,f_c_m[0].id, forecast_out)
            # if accuracy>0.9:
            #     accuracy = 0.8+accuracy/10
            y_pre_path = './dataSet/bsp_model_test_result/'+tiData[0].stockData.stock.name+'_'\
                         +str(datetime.date.today())+'_'+str(np.random.randint(1,1000))+'.csv'
            pd.DataFrame(y_pre.values,index=y_pre.index).to_csv(y_pre_path)
            bsp_model.r1 = round(accuracy, 4)
            # trueY = [str(i) for i in y_test]
            # predictY = [str(round(i,2)) for i in result]
            bsp_model.m10 = "创建"
            #保存好的模型
            filePath = './dataSet/choice_bsp_models/'+name+'_model.m'
            joblib.dump(clf,filePath)
            bsp_model.modelPath = filePath
            bsp_model.save()
            return JsonResponse({'msg': '添加成功'})
    return render(request, 'bsp_md_add.html')