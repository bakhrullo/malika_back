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
        # requests.post()
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
        model = self.request.query_params.get('model')
        return Phone.objects.filter(model=model)


class PhoneList(ListAPIView):
    serializer_class = PhoneSerializer
    queryset = Phone.objects.all()


class OrderUpdate(RetrieveUpdateAPIView):
    serializer_class = OrderUpdateSerializer
    lookup_field = 'id'
    queryset = Order.objects.all()
