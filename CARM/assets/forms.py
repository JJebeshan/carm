from django import forms
import datetime
from .models import Asset_register,Vehicle_listing
from django.forms import modelformset_factory


current_year=datetime.date.today().year
year_choice=[(y,y)for y in range (current_year,1990,-1)]

class AssetRegisterForm(forms.ModelForm):
    class Meta:
        model = Asset_register
        fields = ["Ast_code", "Ast_Type", "Ast_Brand", "Ast_Model", "Ast_Isrent", "Ast_Price", "Ast_document"]

        labels = {
            "Ast_code": "Asset Code",
            "Ast_Type": "Asset Type",
            "Ast_Brand": "Brand",
            "Ast_Model": "Model",
            "Ast_Isrent": "Rentable",
            "Ast_Price": "Purchase Amount (INR)",
            "Ast_document": "Upload Document",
        }

        widgets = {
            "Ast_code": forms.TextInput(attrs={
                "class": "w-full border px-4 py-2 rounded pr-10 bg-gray-100 cursor-not-allowed",
                "placeholder": "{{'Ast_code'}}",
                "id": "assetCode",
                "required": True
            }),
            "Ast_Type": forms.Select(choices=[
                ("", "-- Select Type --"),
                ("Vehicle", "Vehicle"),
                ("Machinery", "Machinery"),
                ("Electronics", "Electronics"),
                ("Furniture", "Furniture"),
                ("Other", "Other"),
            ], attrs={
                "class": "w-full border px-4 py-2 rounded",
                "id": "type",
                "required": True
            }),
            "Ast_Brand": forms.TextInput(attrs={
                "class": "w-full border px-4 py-2 rounded",
                "placeholder": "Tata, HP, Sony...",
                "id": "brand",
                "required": True
            }),
            "Ast_Model": forms.TextInput(attrs={
                "class": "w-full border px-4 py-2 rounded",
                "placeholder": "Model X, Swift Dzire...",
                "id": "model",
                "required": True
            }),
            "Ast_Isrent": forms.RadioSelect(choices=[
                (True, "Yes"),
                (False, "No")
            ], attrs={
                "class": "form-radio text-blue-600"
            }),
            "Ast_Price": forms.NumberInput(attrs={
                "class": "w-full border px-4 py-2 rounded",
                "placeholder": "e.g. 500000",
                "required": True
            }),
            "Ast_document": forms.ClearableFileInput(attrs={
                "class": "w-full border px-4 py-2 rounded bg-gray-50",
                "accept": ".pdf,.doc,.jpg,.png",
            }),
        }

class VehicleForm(forms.ModelForm):
    # Front and Back images are included as ImageFields
    Front_image = forms.ImageField(
        required=True,
        widget=forms.ClearableFileInput(attrs={'class': 'border px-4 py-2 rounded'})
    )
    Back_image = forms.ImageField(
        required=True,
        widget=forms.ClearableFileInput(attrs={'class': 'border px-4 py-2 rounded'})
    )
    year = forms.ChoiceField(
        choices=year_choice,
        widget=forms.Select(attrs={'class': 'border px-4 py-2 rounded'})
    )

    class Meta:
        model = Vehicle_listing
        fields = [
            'Ast_code', 'Plate_no', 'brand', 'model',
            'Vehicle_type', 'Engine_type', 'Fuel_type', 'color',
            'year', 'mileage', 'Purchase', 'Insurance', 'chasis_no',
            'Engine_no', 'Rent', 'meter_In', 'Front_image', 'Back_image'
        ]
        widgets = {
            'Plate_no': forms.TextInput(attrs={'class': 'border px-4 py-2 rounded'}),
            'brand': forms.TextInput(attrs={'class': 'border px-4 py-2 rounded', 'readonly': 'readonly'}),
            'model': forms.TextInput(attrs={'class': 'border px-4 py-2 rounded', 'readonly': 'readonly'}),
            'Vehicle_type': forms.Select(attrs={'class': 'border px-4 py-2 rounded'}),
            'Engine_type': forms.Select(attrs={'class': 'border px-4 py-2 rounded'}),
            'Fuel_type': forms.Select(attrs={'class': 'border px-4 py-2 rounded'}),
            'color': forms.TextInput(attrs={'class': 'border px-4 py-2 rounded'}),
            'mileage': forms.NumberInput(attrs={'class': 'border px-4 py-2 rounded'}),
            'Purchase': forms.NumberInput(attrs={'class': 'border px-4 py-2 rounded', 'readonly': 'readonly'}),
            'Insurance': forms.TextInput(attrs={'class': 'border px-4 py-2 rounded'}),
            'chasis_no': forms.TextInput(attrs={'class': 'border px-4 py-2 rounded'}),
            'Engine_no': forms.TextInput(attrs={'class': 'border px-4 py-2 rounded'}),
            'Rent': forms.NumberInput(attrs={'class': 'border px-4 py-2 rounded'}),
            'meter_In': forms.NumberInput(attrs={'class': 'border px-4 py-2 rounded'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        registered_assets = Vehicle_listing.objects.values_list('Ast_code_id', flat=True)
        self.fields['Ast_code'].queryset = Asset_register.objects.exclude(Ast_code__in=registered_assets)
        self.fields['Ast_code'].widget.attrs.update({'class': 'border px-4 py-2 rounded'})
        self.fields['Ast_code'].required = True
