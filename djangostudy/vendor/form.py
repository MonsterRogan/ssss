from django import forms

from .models import Vendor, Food

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'

class RawVendorForm(forms.Form):
    vendor_name = forms.CharField()
    store_name = forms.CharField()
    phone_number = forms.CharField()