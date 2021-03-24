from django.forms import ModelForm, NumberInput, Select
from .models import Column, Data


class ColumnForm(ModelForm):
    class Meta:
        model = Column
        fields = ("name", "order", "data_type", "range_min", "range_max")
        widgets = {
            'data_type': Select(attrs={"id": "range", "onchange": "what_type()"}),
            'range_min': NumberInput(),
            'range_max': NumberInput(),
        }


class DataForm(ModelForm):
    class Meta:
        model = Data
        fields = ("count",)
