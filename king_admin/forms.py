#__author:  Administrator
#date:  2017/1/10

from django.forms import forms,ModelForm

from crm import models

class CustomerModelForm(ModelForm):
    class Meta:
        model =  models.Customer
        fields = "__all__"




def create_model_form(request,admin_class):
    '''动态生成MODEL FORM'''

    def __new__(cls, *args, **kwargs):

        # super(CustomerForm, self).__new__(*args, **kwargs)
        print("base fields",cls.base_fields)
        for field_name,field_obj in cls.base_fields.items():
            print(field_name,dir(field_obj))
            field_obj.widget.attrs['class'] = 'form-control'
            # field_obj.widget.attrs['maxlength'] = getattr(field_obj,'max_length' ) if hasattr(field_obj,'max_length') \
            #     else ""
        return ModelForm.__new__(cls)

    class Meta:
        model = admin_class.model
        fields = "__all__"
    attrs = {'Meta':Meta}
    _model_form_class =  type("DynamicModelForm",(ModelForm,),attrs)
    setattr(_model_form_class,'__new__',__new__)

    print("model form",_model_form_class.Meta.model )
    return _model_form_class