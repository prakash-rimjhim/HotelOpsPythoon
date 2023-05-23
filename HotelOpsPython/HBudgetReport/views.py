from datetime import date
from django.shortcuts import render,redirect
from .models import Outlet,Expenses

def index(request):
    mem = Outlet.objects.filter(IsDelete=False)
    return render(request, 'index.html' ,{'mem' :mem})

def add(request):
    if request.method == "POST":
        title = request.POST['title']
        obj = Outlet.objects.create(title = title)
        obj.save()
        return (redirect('/'))
    
    return render(request,'add.html')

    
def delete(request,id):
    mem = Outlet.objects.get(id = id)
    mem.IsDelete=True
    mem.ModifyBy=1
    mem.save()
    #mem.delete()
    return redirect('/')


def update(request , id):
    mem = Outlet.objects.get(id = id)
    return render(request,'update.html',{'mem':mem})

def updata (request , id):
    title = request.POST["title"]
    mem = Outlet.objects.get(id = id)
    mem.title = title
    mem.save()
    
    return redirect("/")
 
 
 


def expenses(request):
    rem = Expenses.objects.all()
    return render(request, 'expenses.html' ,{'rem' :rem})


def add_expenses(request):
    if request.method == "POST":
        title = request.POST['title']
        obj = Expenses.objects.create(title = title)
        obj.save()
        return (redirect('/expenses'))
    return render(request,'add_expenses.html')
    
def delete_expenses(request,id):
    rem = Expenses.objects.get(id = id)
    rem.delete()
    return redirect('/expenses')



def update_expenses(request , id):
    if request.method == "POST":
        title = request.POST["title"]
        rem = Expenses.objects.get(id = id)
        rem.title = title
        rem.save()    
        return redirect("/expenses")
    rem = Expenses.objects.get(id = id)
    return render(request,'update_expenses.html',{'rem':rem})

# def updata_expenses(request , id):
#     title = request.POST["title"]
#     rem = Expenses.objects.get(id = id)
#     rem.title = title
#     rem.save()    
#     return redirect("/expenses")


 