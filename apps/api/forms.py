from wtforms import Form
from wtforms_alchemy import model_form_factory


from apps.models import *


ModelForm = model_form_factory(Form)


class ProductForm(ModelForm):
    class Meta:
        model = Product


class DiscountForm(ModelForm):
    class Meta:
        model = Discount

