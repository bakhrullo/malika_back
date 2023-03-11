from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.views import APIView

import requests

from .serializers import *


class OrderCreate(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if request.get_full_path() == "/api/v1/order/create":
            requests.post(url="http://127.0.0.1:8090/api/v1/order/create", data=serializer.data)
        return Response(serializer.data)


class OrderCheck(ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        order_id = self.kwargs['id']
        return [Order.objects.get(id=order_id)]


class ModelList(ListAPIView):
    serializer_class = PhoneSerializer

    def get_queryset(self):
        return Phone.objects.order_by('model').distinct('model')


class PhoneFilter(ListAPIView):
    serializer_class = PhoneSerializer

    def get_queryset(self):
        model, name = self.request.query_params.get('model'), self.request.query_params.get('name')
        if model != "default":
            return Phone.objects.filter(model=model)
        elif name != "default":
            return Phone.objects.filter(name=name)


class PhoneList(ListAPIView):
    serializer_class = PhoneSerializer
    queryset = Phone.objects.all()


class OrderUpdate(RetrieveUpdateAPIView):
    serializer_class = OrderUpdateSerializer
    lookup_field = 'id'
    queryset = Order.objects.all()
