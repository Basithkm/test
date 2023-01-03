from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('logout',views.logout,name='logout'),
    path('insert',views.insert,name='insert'),
    path('update/<int:id>',views.update_data,name='update_data'),
    path('delete/<int:id>',views.delete_data,name='delete_data'),
    path('imagelist',views.image_list,name= 'image_list'),
    path('fulldetails/<int:id>',views.individual_details,name='individual_details')
    
]

