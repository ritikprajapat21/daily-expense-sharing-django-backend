from django.urls import path

from . import views

urlpatterns = [
    path('add', views.add_user),
    path('<int:id>', views.get_user),
    path('expense', views.get_overall_expense),
    path('expense/all', views.get_expenses),
    path('expense/<int:id>', views.get_expense),
    path('expense/add', views.add_expense),
    path('split', views.set_split),
]
