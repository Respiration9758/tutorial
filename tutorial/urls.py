"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from snippets import views
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'zixuns', views.ZixunViewSet)
router.register(r'pictures', views.PictureViewSet)
router.register(r'sss', views.SSViewSet)
# from django.conf.urls import path

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^ss_list$', views.ss),
    url(r'^ss_add$', views.ss_add, name='ss_add'),
    url(r'^ss_edit/', views.ss_edit, name='ss_edit'),
    url(r'^register$', views.register),
    url(r'^upload_file$', views.upload_file),
    url(r'^login_out$', views.logout_view),
    url(r'^login$', views.login_index),
    url(r'^register$', views.register),
    url(r'^registerSub$', views.registerSub),
    url(r'^index$', views.index),
    url(r'^picture_add$', views.picture_add, name='picture_add'),
    url(r'^picture_show$', views.picture_show, name='picture_show'),
    url(r'^picture_list$', views.picture_list, name='picture_list'),
    url(r'^artical_list$', views.artical_list, name='artical_list'),
    url(r'^article_add$', views.article_add, name='article_add'),
    url(r'^welcome$', views.welcome, name='welcome'),
    #url(r'^api/', include(router.urls)),
    url(r'^api/', include((router.urls))),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-auth/', include(('rest_framework.urls'), namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^admin/', admin.site.urls),

    url(r'^charts1$',views.charts1),
    url(r'^charts2$',views.charts2),
    url(r'^charts3$',views.charts3),
    url(r'^charts4$',views.charts4),
    url(r'^charts5$',views.charts5),
    url(r'^charts6$',views.charts6),
    url(r'^charts7$',views.charts7),
    url(r'^Echarts1$',views.Echarts1),
    url(r'^Echarts2$',views.Echarts2),
    url(r'^Echarts3$',views.Echarts3),

    url(r'^admin-role$',views.adminRole),
    url(r'^admin-permission$',views.adminPermission),
    url(r'^admin-list$',views.adminList),
    url(r'^admin-add$',views.adminAdd),
    url(r'^admin-submit$',views.adminSubmit),

    url(r'^data_search/(.+)/$',views.data_search),
    url(r'^data_search2/(.+)/$',views.data_search2),
    url(r'^data_search3/(.+)/$', views.data_search3),

    url(r'^sto_list$', views.sto),
    url(r'^sto_add$', views.sto_add, name='sto_add'),
    url(r'^sto_submit$',views.sto_submit,name='sto_submit'),
    url(r'sto_delete/(.+)/$',views.sto_delete,name='sto_delete'),

    url(r'^sd_list$', views.stockData_list,name='sd_list'),
    url(r'^sd_add$', views.sd_add, name='sd_add'),
    url(r'^sd_submit$',views.sd_submit,name='sd_submit'),
    url(r'^sd_delete/(.+)/$',views.sd_delete,name='sd_delete'),
    url(r'^sd_append/(.+)/$',views.sd_append,name='sd_append'),

    url(r'^cw_list$', views.stockCWData_list,name='cw_list'),
    url(r'^cw_add$', views.cw_add, name='cw_add'),
    url(r'^cw_submit$',views.cw_submit,name='cw_submit'),
    url(r'^cw_delete/(.+)/$',views.cw_delete,name='cw_delete'),

    url(r'^tl_list$',views.technical_list,name='tl_list'),
    url(r'^tl_add$', views.tl_add, name='tl_add'),
    url(r'^tl_submit$',views.tl_submit,name='tl_submit'),
    url(r'^tl_delete/(.+)/$',views.tl_delete,name='tl_delete'),

    url(r'^td_list$',views.technicalData_list,name='td_list'),
    url(r'^td_add$', views.td_add, name='td_add'),
    url(r'^td_submit$',views.td_submit,name='td_submit'),
    url(r'^td_delete/(.+)/$',views.td_delete,name='td_delete'),

    url(r'^stra_list$',views.strategy_list,name='stra_list'),
    url(r'^stra_add$', views.stra_add, name='stra_add'),
    url(r'^stra_train$',views.stra_train,name='stra_train'),
    url(r'^stra_upload$', views.stra_upload, name='stra_upload'),
    url(r'^stra_submit$',views.stra_submit,name='stra_submit'),
    url(r'^stra_delete/(.+)/$',views.stra_delete,name='stra_delete'),

    url(r'^sp_list$',views.sp_list,name='sp_list'),
    url(r'^sp_add$', views.sp_add, name='sp_add'),
    url(r'^sp_delete/(.+)/$',views.sp_delete,name='sp_delete'),

    url(r'^al_list$', views.algorithm_list,name='al_list'),
    url(r'^al_add$', views.al_add, name='al_add'),
    url(r'^al_submit$',views.al_submit,name='al_submit'),
    url(r'^al_delete/(.+)/$',views.al_delete,name='al_delete'),

    url(r'^md_list$', views.model_list,name='md_list'),
    url(r'^md_add$', views.md_add, name='md_add'),
    url(r'^md_submit$',views.md_submit,name='md_submit'),
    url(r'^md_delete/(.+)/$',views.md_delete,name='md_delete'),
    url(r'^md_visual/(.+)/$$',views.md_visual,name='md_visual'),
    url(r'^md_upload$', views.md_upload, name='md_upload'),
    url(r'^md_uploadSub$', views.md_uploadSub, name='md_uploadSub'),

    url(r'^mp_list$', views.mp_list, name='mp_list'),
    url(r'^mp_contrast$', views.mp_contrast, name='mp_contrast'),
    url(r'^mp_add$', views.mp_add, name='mp_add'),
    url(r'^mp_submit$', views.mp_submit, name='mp_submit'),
    url(r'^mp_delete/(.+)/$', views.mp_delete, name='mp_delete'),

    url(r'^css_list$', views.css_list, name='css_list'),
    url(r'^cts_list$', views.cts_list, name='cts_list'),

    url(r'^cs_p_v$', views.cs_p_v, name='cs_p_v'),
    url(r'^r_test$', views.r_test, name='r_test'),
    url(r'^user_analysis$', views.user_analysis, name='user_analysis'),

    url(r'^bsp_al_list$', views.bsp_al_list, name='bsp_al_list'),
    url(r'^bsp_md_list$', views.bsp_md_list, name='bsp_md_list'),
    url(r'^bsp_mp_list$', views.bsp_mp_list, name='bsp_mp_list'),

    url(r'^f_c_list$', views.f_c_list, name='f_c_list'),
    url(r'^bsp_r_list$', views.bsp_r_list, name='bsp_r_list'),
    url(r'^trend_r_list$', views.trend_r_list, name='trend_r_list'),

    url(r'^bsp_md_vis/(.+)/$', views.bsp_md_vis, name='bsp_md_vis'),
    url(r'^bsp_md_add$', views.bsp_md_add, name='bsp_md_add'),
    url(r'^bsp_md_submit$', views.bsp_md_submit, name='bsp_md_submit')

]
