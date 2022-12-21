from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from .models import Vendor
from .form import VendorForm
from .form import RawVendorForm
from django.utils.translation import gettext_lazy as _
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

# Create your views here.
def index(request):
    return HttpResponse("HEPP")

def showtemplate(request):
    vendor_list = Vendor.objects.all()
    context = {'vendor_list' : vendor_list}
    return render(request, 'vendor\detail.html', context)


# 針對 vendor_create.html
def vendor_create_view(request):
    form = RawVendorForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        Vendor.objects.create(**form.cleaned_data)
        # form.save()
        form = RawVendorForm()

    context = {
        'form' : form
    }
    return render(request, "vendor_create.html", context)

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
        # 新增 labels 對應
        labels = {
            'vendor_name': _('攤販名稱'),
            'store_name' : _('店名'),
            'phone_number' : _('電話'),
            'address' : _('地址'),
        }

def singleVendor(request, id):
    vendor_list = get_object_or_404(Vendor, id = id)
    # try:
    #     vendor_list = Vendor.objects.get(id = id)
    # except Vendor.DoesNotExist:
    #      raise Http404
    context = {
        'vendor_list': vendor_list
    }
    return render(request, 'vendor/detail.html', context)

class VendorListView(ListView):
    model = Vendor
    template_name = 'vendor/vendor_list.html'

# 繼承 DetailView
class VendorDetail(DetailView):
    model = Vendor
    # queryset = Vendor.objects.all()
    template_name = 'vendor/detail.html'