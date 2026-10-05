from django import forms

from .models import WarehouseModel


class WarehouseModelForm(forms.ModelForm):
    class Meta:
        model = WarehouseModel
        fields = ["name", "floor_width_m", "floor_depth_m", "notes"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "floor_width_m": forms.NumberInput(attrs={"class": "form-control", "step": "0.5"}),
            "floor_depth_m": forms.NumberInput(attrs={"class": "form-control", "step": "0.5"}),
            "notes": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
        }
