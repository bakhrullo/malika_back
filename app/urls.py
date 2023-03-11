from django.urls import path

from .views import *

urlpatterns = [
    path('api/v1/order/create', OrderCreate.as_view()),
    path('api/v1/order/create/bot', OrderCreate.as_view()),
    path('api/v1/order/status/<int:id>', OrderCheck.as_view()),
    path('api/v1/model/list', ModelList.as_view()),
    path('api/v1/phones/list', PhoneList.as_view()),
    path('api/v1/phones/filter', PhoneFilter.as_view()),
    path('api/v1/order/update/<int:id>', OrderUpdate.as_view()),
]
