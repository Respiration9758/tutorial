# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Choice_s_strategy, Choice_t_strategy, feature_c_method, trend_c_method, bsp_c_method, BSP_Algorithm,BSP_Predict_Model,BSP_Pre_Result
from django.contrib import admin

# Register your models here.
admin.site.register(Choice_t_strategy)
admin.site.register(Choice_s_strategy)
admin.site.register(feature_c_method)
admin.site.register(bsp_c_method)
admin.site.register(trend_c_method)
admin.site.register(BSP_Pre_Result)
admin.site.register(BSP_Predict_Model)
admin.site.register(BSP_Algorithm)