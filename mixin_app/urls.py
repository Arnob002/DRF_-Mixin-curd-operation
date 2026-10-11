from django.urls import path
from mixin_app.views import *

urlpatterns = [
    path('employee/',employee.as_view(),name='employees'),
    path('employee/<str:pk>/',employeeDetail.as_view(),name='employee'),
]