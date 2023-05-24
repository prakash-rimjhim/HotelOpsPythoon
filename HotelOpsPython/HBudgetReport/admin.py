from django.contrib import admin
from .models import Outlet,Expenses,PayrollExpenses,PayrollExpensesEntry

admin.site.register(Outlet)
admin.site.register(Expenses)
admin.site.register(PayrollExpenses)
admin.site.register(PayrollExpensesEntry)
