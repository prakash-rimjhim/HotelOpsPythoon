from django.urls import path
from .import views

urlpatterns = [
    path('', views.index , name = 'index'),
    path('outlet/', views.index , name = 'index'),
    path('add/',views.add , name ='add'),
    path('delete/<int:id>/' , views.delete , name = 'delete'),
    path('update/<int:id>/',views.update,name= "update"),
    path('update/updata/<int:id>/',views.updata , name = "updata"),
    
    path('expenses/', views.expenses , name = 'expenses'),
    path('add_expenses', views.add_expenses , name = 'add_expenses'),
    path('delete_expenses/<int:id>/' , views.delete_expenses , name = 'delete_expenses'),
    path('update_expenses/<int:id>/',views.update_expenses , name= "update_expenses"),
    # path('update_expenses/updata_expenses/<int:id>/',views.updata_expenses , name = "updata_expenses"),
    
     
]