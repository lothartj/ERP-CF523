from django.shortcuts import render, redirect, get_object_or_404
from .models import Items, Login
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(Login ,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('main')
        


    return render(request, 'erpapp/login.html')

@login_required(login_url='login/')
def newitem(request):
    if request.method == 'POST':
        itemcode = request.POST.get('itemcode')
        description = request.POST.get('description')
        barcode = request.POST.get('barcode')
        unitmeasure = request.POST.get('unitmeasure')
        inventory = request.POST.get('inventory')
        unitcost = request.POST.get('unitcost')
        image = request.FILES.get('image_field')

        if not itemcode or not description or not barcode or not unitmeasure or not inventory or not unitcost or not image:
            messages.error(request, 'Please Fill in all inputs')
            return render(request, 'newitem')
        else:
            save = Items(itemcode=itemcode,description=description,barcode=barcode,unitmeasure=unitmeasure,inventory=inventory,unitcost=unitcost, image=image)
            save.save()
            return redirect('main')
    
    return render(request, 'erpapp/newitem.html')



@login_required(login_url='login/')
def user_main(request):
    items =  Items.objects.all()
    return render(request, 'erpapp/main.html', {'items':items})

@login_required(login_url='login/')
def viewitem(request, item_id):
    item = get_object_or_404(Items, id=item_id)
    return render(request, 'erpapp/viewitem.html', {'item': item})

def delete_item(request ,item_id):
    item = Items.objects.get(id=item_id)
    item.delete()
    return redirect('main')

from django.shortcuts import render


def my_view(request, item_id):
    item = Items.objects.get(id=item_id)  # or however you're fetching the object
    return render(request, 'viewitem', {'item': item})
