from django.shortcuts import render, redirect
from  . models import Product
from . forms import ProductForm
# Create your views here.
def index2(request):
    product=Product.objects.all()
    context={
        'product_list':product
    }
    return render(request, 'index2.html', context)
def detail2(request,product_id):
    product=Product.objects.get(id=product_id)
    return render(request,"detail2.html",{'product': product})
def add_product(request):
    if request.method=="POST":
        name = request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        price = request.POST.get('price',)
        img = request.FILES['img']
        product=Product(name=name,desc=desc,year=year,img=img,price=price)
        product.save()
    return render(request, 'add2.html')

def update2(request,id):
    product=Product.objects.get(id=id)
    form=ProductForm(request.POST or None, request.FILES, instance=product)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit2.html',{'form':form,'product':product})
def delete2(request,id):
    if request.method=='POST':
        product=Product.objects.get(id=id)
        product.delete()
        return redirect('/')
    return render(request,'delete2.html')