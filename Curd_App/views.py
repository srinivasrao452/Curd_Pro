from django.shortcuts import render
from .forms import InsertingDataForm,DeletingDataForm,UpdatingDataForm
from .models import ProductData
from django.http.response import HttpResponse

def main_page(request):
    return render(request,'main_page.html')


def insertingdata_view(request):
    if request.method =="POST":
        iform = InsertingDataForm(request.POST)
        if iform.is_valid():
            product_number = request.POST.get('product_number','')
            product_name = request.POST.get('product_name','')
            product_cost = request.POST.get('product_cost','')
            product_class = request.POST.get('product_class','')
            product_weight = request.POST.get('product_weight','')

            data = ProductData(
                product_name=product_name,
                product_number=product_number,
                product_cost=product_cost,
                product_class=product_class,
                product_weight=product_weight
            )
            data.save()
            iform = InsertingDataForm()
            return render(request, 'insertingdata.html', {'iform': iform})
    else:
        iform = InsertingDataForm()
        return render(request,'insertingdata.html',{'iform':iform})


def retrieveingdata_view(request):
    pdata = ProductData.objects.all()
    return render(request,'retrieveingdata.html',{'pdata':pdata})


def updatingdata_view(request):
    if request.method == "POST":
        uform = UpdatingDataForm(request.POST)
        if uform.is_valid():
            product_number = request.POST.get('product_number','')
            product_cost = request.POST.get('product_cost','')

            pnum = ProductData.objects.filter(product_number=product_number)

            if not pnum:
                return HttpResponse("Product Is Not Available")
            else:
                pnum.update(product_cost=product_cost)
                uform = UpdatingDataForm()
                return render(request, 'updatingdata.html', {'uform': uform})
    else:
        uform = UpdatingDataForm()
        return render(request,'updatingdata.html',{'uform':uform})

def deletingdata_view(request):
    if request.method == "POST":
        dform = DeletingDataForm(request.POST)
        if dform.is_valid():
            product_number = request.POST.get('product_number','')

            pnum = ProductData.objects.filter(product_number=product_number)

            if not pnum:
                return HttpResponse("Invalid Product Number")
            else:
                pnum.delete()
                dform = DeletingDataForm()
                return render(request,'deletingdata.html',{'dform':dform})
    else:
        dform = DeletingDataForm()
        return render(request,'deletingdata.html',{'dform':dform})



