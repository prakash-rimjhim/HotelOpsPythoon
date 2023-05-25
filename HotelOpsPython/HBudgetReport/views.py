from datetime import date
from django.shortcuts import render,redirect
from .models import Outlet,Expenses,PayrollExpenses, PayrollExpensesEntry,PLUtilitiesMaster

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


def payrollExpenses(request):
    mem = PayrollExpenses.objects.filter(IsDelete=False)
    return render(request, 'payrollExpenses.html' ,{'mem' :mem})

def add_payrollExpenses(request):
    if request.method == "POST":
        title = request.POST['title']
        obj = PayrollExpenses.objects.create(title = title)
        obj.save()
        return (redirect('/PayrollExpenses'))
    return render(request,'add_payrollExpenses.html')

def delete_payrollExpenses(request,id):
    mem = PayrollExpenses.objects.get(id = id)
    mem.IsDelete = True
    mem.ModifyBy = 1
    mem.save()
    return (redirect('/PayrollExpenses'))

def update_payrollExpenses(request , id):
    if request.method == "POST":
        title = request.POST["title"]
        rem = PayrollExpenses.objects.get(id = id)
        rem.title = title
        rem.save()    
        return (redirect('/PayrollExpenses'))
    rem = PayrollExpenses.objects.get(id = id)
    return render(request,'update_PayrollExpenses.html',{'rem':rem})
    
    

def PayrollExpenseEntry(request):
    if request.method == "POST":
        TotalItem = request.POST["TotalItem"]
        for x in range(int(TotalItem)):
            Amount=request.POST["Amount_"+str(x)]
            ExpenseID=request.POST["ExpenseID_"+str(x)]
            v=PayrollExpenses.objects.get(id=ExpenseID)
            obj = PayrollExpensesEntry.objects.create(ExpenseID =v ,Amount=Amount)
            obj.save()
        
        # title = request.POST['title']
        # obj = Outlet.objects.create(title = title)
        # obj.save()
        #return (redirect('/'))
    mem = PayrollExpenses.objects.filter(IsDelete=False)
    return render(request,'PayrollExpenseEntry.html',{'mem' :mem})


        
def pLUtilitiesMaster(request):
    mem = PLUtilitiesMaster.objects.filter(IsDelete = False)
    return render(request , 'plutilities.html',{'mem':mem})
    
def add_plutilities(request):
    if request.method == "POST":
        title = request.POST['title']
        obj = PLUtilitiesMaster.objects.create(title = title)
        obj.save()
        return (redirect('/PLUtilitiesMaster'))
    return render(request,'add_plutilities.html')


def delete_plutilities(request,id):
    mem = PLUtilitiesMaster.objects.get(id = id)
    mem.IsDelete = True
    mem.ModifyBy = 1
    mem.save()
    return (redirect('/PLUtilitiesMaster'))
    

def update_plutilities(request , id):
    if request.method == "POST":
        title = request.POST["title"]
        mem = PLUtilitiesMaster.objects.get(id = id)
        mem.title = title
        mem.save()    
        return (redirect('/PLUtilitiesMaster'))
    mem = PLUtilitiesMaster.objects.get(id = id)
    return render(request,'update_plutilities.html',{'mem':mem})

def PutilitiesEntry(request):
    if request.method == "POST":
        TotalItem = request.POST["TotalItem"]
        for x in range(int(TotalItem)):
            Amount = request.POST["Amount_" + str(x)]
            ExpenseID = request.POST["Expense_ID" + str(x)]
            v = PLUtilitiesMaster.objects.get(id = ExpenseID)
            obj = PLUtilitiesMaster.objects.create(ExpenseID = v , Amount = Amount)
            obj.save()
    mem = PLUtilitiesMaster.objects.filter(IsDelete = False)
    return render(request, 'PLUtilitiesEntry.html' ,{'mem':mem})
            
    
    
    
        
        
    