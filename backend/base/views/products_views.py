from base.models import Product
from rest_framework.decorators import api_view,permission_classes

from rest_framework.response import Response
from base.serializer import ProductSerializer
# Create your views here.

from django.contrib.auth.hashers import mask_hash
from rest_framework import status

@api_view(['GET'])
def getrPoducts(request):
    products=Product.objects.all()
    serializer=ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, pk):
    product= Product.objects.get(_id=pk)
    serializer=ProductSerializer(product,many=False)
    return Response(serializer.data)

