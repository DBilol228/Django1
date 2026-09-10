from django.shortcuts import render,redirect
from .models import Category,Product,Customer

def home(request):
    return render(request,'home.html')

def categories(request):
    categories = Category.objects.all()
    return render(request,'categories.html',{'categories':categories})


def category_detail(request,id):
    category = Category.objects.get(id=id)
    return render(request,'category_detail.html',{'category':category})

def create_category(request):
    if request.method=='POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        Category.objects.create(name=name,description=description)
        return redirect('categories')
    return render(request,'category_create.html')

def update_category(request,id):
    category = Category.objects.get(id=id)
    if request.method=='POST':
        new_name=request.POST.get('name')
        new_description=request.POST.get('description',category.description) 
        category.name=new_name
        category.description = new_description
        category.save()
        return redirect('categories')
    return render(request,'category_update.html',{'category':category})

def delete_category(request,id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('categories')



def products(request):
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    products = Product.objects.all()
    if min_price:
        products = products.filter(price__gte = min_price)
    if max_price:
        products = products.filter(price__lte = max_price)
    search = request.GET.get('search')
    if search:
        products = products.filter(name__icontains = search)
    return render(request,'products.html',{'products':products})

def product_detail(request,id):
    product = Product.objects.get(id=id)
    return render(request,'product_detail.html',{'product':product})

def create_product(request):
    if request.method=='POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        price=request.POST.get('price')
        quantity=request.POST.get('quantity')
        Product.objects.create(name=name,description=description,price=price,quantity=quantity)
        return redirect('products')
    return render(request,'product_create.html')

def update_product(request,id):
    product = Product.objects.get(id=id)
    if request.method=='POST':
        new_name=request.POST.get('name')
        new_description=request.POST.get('description',product.description) 
        new_price = request.POST.get('price')
        new_quantity = request.POST.get('quantity')
        product.name=new_name
        product.description = new_description
        product.price = new_price
        product.quantity = new_quantity
        product.save()
        return redirect('products')
    return render(request,'product_update.html',{'product':product})

def delete_product(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('products')



def customers(request):
    customers = Customer.objects.all()
    return render(request,'products.html',{'customers':customers})

def customer_detail(request,id):
    customer = Customer.objects.get(id=id)
    return render(request,'customer_detail.html',{'customer':customer})

def create_customer(request):
    if request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        Product.objects.create(name=name,phone=phone,address=address)
        return redirect('customers')
    return render(request,'customer_create.html')

def update_customer(request,id):
    customer = Product.objects.get(id=id)
    if request.method=='POST':
        new_name=request.POST.get('name')
        new_phone=request.POST.get('phone',customer.phone) 
        new_address = request.POST.get('address')
        customer.name=new_name
        customer.phone = new_phone
        customer.address = new_address
        customer.save()
        return redirect('customers')
    return render(request,'customer_update.html',{'customer':customer})

def delete_customer(request,id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect('customer')