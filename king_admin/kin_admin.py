# from crm import models
#
# enabled_admins = {}
#
# class BaseAdmin(object):
#     list_display = []
#     list_filter = []
#
# class CustomerAdmin(BaseAdmin):
#     list_display = ['qq','name','source','consultant','consult_course','date','status']
#     list_filters = ['source','consultant','consult_course','status','date']
#     search_fields = ['qq','name',"consultant__name"]
#     #model = models.Customer
#     list_per_page = 5
#     ordering = "qq"
#
# class CustomerFollowUpAdmin(BaseAdmin):
#     list_display = ['customer','consultant','date']
#
# def register(model_class,admin_class=None):
#      if  model_class._meta.app_label not in enabled_admins:
#          enabled_admins[model_class._meta.app_label] = {}#enabled_admin['crm'] = {}
#
#      #admin_obj = admin_class()
#      admin_class.model = model_class #绑定model对象和admin类
#      enabled_admins[model_class._meta.app_label][model_class._meta.model_name] = admin_class #enabled_admins['crm']['customerfollowup'] = CustomerFollowUpAdmin
#
# register(models.Customer,CustomerAdmin)
# register(models.CustomerFollowUp,CustomerFollowUpAdmin)
#
# #print(enabled_admins)

#__author:  Administrator
#date:  2017/1/5

from crm import models


enabled_admins = {}

class BaseAdmin(object):
    list_display = []
    list_filters = []
    search_fields = []
    list_per_page = 20
    ordering = None

class CustomerAdmin(BaseAdmin):
    list_display = ["id",'qq','name','source','consultant','consult_course','date','status']
    list_filters = ['source','consultant','consult_course','status','date']
    search_fields = ['qq','name',"consultant__name"]

    #model = models.Customer
    list_per_page = 5
    ordering = "qq"
class CustomerFollowUpAdmin(BaseAdmin):
    list_display = ('customer','consultant','date')


def register(model_class,admin_class=None):
    if model_class._meta.app_label not in enabled_admins:
        enabled_admins[model_class._meta.app_label] = {} #enabled_admins['crm'] = {}
    #admin_obj = admin_class()
    admin_class.model = model_class #绑定model 对象和admin 类
    enabled_admins[model_class._meta.app_label][model_class._meta.model_name] = admin_class
    #enabled_admins['crm']['customerfollowup'] = CustomerFollowUpAdmin


register(models.Customer,CustomerAdmin)
register(models.CustomerFollowUp,CustomerFollowUpAdmin)


