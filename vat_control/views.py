from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import VAT
from .serializers import VATSerializers


def price(s):
    sum=0
    k=s.split(',')
    for i in k:
        x=i.split()
        sum+=int(x[1])
    return sum

class VATView(APIView):
    def post(self,request):
        s=request.data['items']
        total_cost=price(s)
        v=int(request.data['vat'])
        d=int(request.data['discount'])
        vat_count=total_cost*(v/100)
        dis_count=total_cost*(d/100)
        pr=(total_cost+vat_count)-dis_count
        request.data['total_amount']=pr
        request.data['vat']=vat_count
        request.data['discount']=dis_count
        #print(request.data['total_amount'],request.data['vat'],request.data['discount'])
        serializer=VATSerializers(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response({"Message":"error!"})




