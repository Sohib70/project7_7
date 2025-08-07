# funksiya, Apiview , generic mixins va sz
from django.contrib.admin.templatetags.admin_list import pagination
from django.core.serializers import serialize
from django.shortcuts import render
from django.template.context_processors import request
from rest_framework.decorators import api_view
from unicodedata import category
from .models import Sumka,Category
from .serializers import Sumkaserializers,CategorySerializers
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ListCreateMixins(mixins.ListModelMixin,mixins.CreateModelMixin,GenericAPIView):
    queryset  = Sumka.objects.all()
    serializer_class = Sumkaserializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['category','price']
    search_fields = ['firmasi']
    ordering_fields = ['price','firmasi']
    ordering = ['price']


    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class DetailUpdateDeleteMixins(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,GenericAPIView):
    queryset = Sumka.objects.all()
    serializer_class = Sumkaserializers

    def get(self,request,pk):
        return self.retrieve(request,pk = pk)

    def put(self,request,pk):
        return self.update(request,pk = pk)

    def patch(self,request,pk):
        return self.partial_update(request,pk = pk)

    def delete(self,request,pk):
        return self.destroy(request,pk = pk)


# <----------------------------------------------------------------->

# class ListCreateGenApiView(GenericAPIView):
#     queryset = Sumka.objects.all()
#     serializer_class = Sumkaserializers
#
#     def get(self,request):
#         sumkalar = self.get_queryset()
#         category = request.GET.get('category')
#         price = request.GET.get('price')
#         search = request.GET.get('search')
#         ordering = request.GET.get('ordering')
#
#         if category:
#             sumkalar = sumkalar.filter(category=category)
#
#         if price:
#             sumkalar = sumkalar.filter(price = price)
#
#         if search:
#             sumkalar = sumkalar.filter(Q(nomi__icontains = search) | Q(price__icontains = search))
#
#         if ordering:
#             sumkalar = sumkalar.order_by(ordering)
#         paginator = PageNumberPagination()
#         paginator.page_size = 5
#         result_page = paginator.paginate_queryset(sumkalar,request)
#         serializers = Sumkaserializers(result_page , many=True)
#         return paginator.get_paginated_response(serializers.data)
#
#     def post(self,request):
#         serializers = self.get_serializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data,status=status.HTTP_200_OK)
#         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
#
# class DetailUpdateDeleteGenApiView(GenericAPIView):
#     queryset = Sumka.objects.all()
#     serializer_class = Sumkaserializers
#
#     def get_object(self,pk):
#         Sumka = Sumka.objects.get(pk=pk)
#         return Sumka
#
#     def get(self,request,pk):
#         Sumka = self.get_object(pk=pk)
#         serializer = Sumkaserializers(Sumka)
#         return Response({'data':serializer.data,'status':status.HTTP_200_OK})
#
#     def put(self,request,pk):
#         Sumka = self.get_object(pk=pk)
#         serializer = Sumkaserializers(Sumka,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'data':serializer.data,'status':status.HTTP_200_OK})
#         return Response({'error':serializer.errors,'status':status.HTTP_400_BAD_REQUEST})
#
#     def patch(self,request,pk):
#         Sumka = self.get_object(pk=pk)
#         serializer = Sumkaserializers(Sumka,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'data':serializer.data,'status':status.HTTP_200_OK})
#         return Response({'error':serializer.errors,'status':status.HTTP_400_BAD_REQUEST})
#
#     def delete(self,request,pk):
#         Sumka = self.get_object(pk=pk)
#         Sumka.delete()
#         return Response({'status':status.HTTP_200_OK})

# <------------------------------------------------------------------------->
# class ListCreateApiView(APIView):
#     def get(self,request):
#         sumkalar = Sumka.objects.all()
#         category = request.GET.get('category')
#         price = request.GET.get('price')
#         price_gt = request.GET.get('price_gt')
#         price_lt = request.GET.get('price_lt')
#         search = request.GET.get('search')
#         ordering = request.GET.get('ordering')
#         if category:
#             sumkalar = sumkalar.filter(category = category)
#         if price:
#             sumkalar = sumkalar.filter(price = price)
#         if price_gt:
#             sumkalar = sumkalar.filter(price_gt = price__gt)
#         if price_lt:
#             sumkalar = sumkalar.filter(price_lt = price__lt)
#         if search:
#             sumkalar = sumkalar.filter(Q(firmasi__icontains=search) | Q(price__icontains=search))
#         if ordering:
#             sumkalar = sumkalar.order_by("ordering")
#         paginator = PageNumberPagination()
#         paginator.page_size = 5
#         result_page = paginator.paginate_queryset(sumkalar,request)
#         serializers = Sumkaserializers(result_page , many=True)
#         return paginator.get_paginated_response(serializers.data)
#
#
#     def post(self,request):
#         serializers = Sumkaserializers(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response({"data": serializers.data, "status": status.HTTP_201_CREATED})
#         return Response({"data": serializers.data, "status": status.HTTP_400_BAD_REQUEST})
#
# class DetailUpdateDelete(APIView):
#     def get(self,request,pk):
#         sumka = Sumka.objects.get(pk = pk)
#         serializers = Sumkaserializers(sumka)
#         return Response({"data": serializers.data, "status": status.HTTP_200_OK})
#
#     def put(self,request,pk):
#         sumka = Sumka.objects.get(pk = pk)
#         serializers = Sumkaserializers(sumka,data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response({"data": serializers.data, "status": status.HTTP_200_OK})
#         return Response({"data": serializers.data, "status": status.HTTP_400_BAD_REQUEST})
#
#     def patch(self,request,pk):
#         sumka = Sumka.objects.get(pk = pk)
#         serializers = Sumkaserializers(sumka,data=request.data,partial=True)
#         if serializers.is_valid():
#             serializers.save()
#             return Response({"data": serializers.data, "status": status.HTTP_200_OK})
#         return Response({"data": serializers.data, "status": status.HTTP_400_BAD_REQUEST})
#
#     def delete(self,request,pk):
#         sumka = Sumka.objects.get(pk=pk)
#         sumka.delete()
#         return Response(status = status.HTTP_200_OK)

# <------------------------------------------------------------------------->
#                 funksiya bilan

# @api_view(["GET"])
# def sumka_list(request):
#     sumkalar = Sumka.objects.all()
#     category = request.GET.get('category')
#     price = request.GET.get('price')
#     price_gt = request.GET.get('price_gt')
#     price_lt = request.GET.get('price_lt')
#     search = request.GET.get('search')
#     ordering = request.GET.get('ordering')
#     if category:
#         sumkalar = sumkalar.filter(category = category)
#     if price:
#         sumkalar = sumkalar.filter(price = price)
#     if price_gt:
#         sumkalar = sumkalar.filter(price_gt = price__gt)
#     if price_lt:
#         sumkalar = sumkalar.filter(price_lt = price__lt)
#     if search:
#         sumkalar = sumkalar.filter(Q(firmasi__icontains=search) | Q(price__icontains=search))
#     if ordering:
#         sumkalar = sumkalar.order_by("ordering")
#     paginator = PageNumberPagination()
#     paginator.page_size = 5
#     result_page = paginator.paginate_queryset(sumkalar,request)
#     serializers = Sumkaserializers(result_page , many=True)
#     return paginator.get_paginated_response(serializers.data)
#
# @api_view(["POST"])
# def sumka_post(request):
#     serializers = Sumkaserializers(data=request.data)
#     if serializers.is_valid():
#         serializers.save()
#         return Response({"data": serializers.data, "status": status.HTTP_200_OK})
#     return Response({"data":serializers.data,"status":status.HTTP_400_BAD_REQUEST})
#
# @api_view(["GET"])
# def sumka_detail(request,pk):
#     sumka = Sumka.objects.get(id=pk)
#     serializers = Sumkaserializers(sumka)
#     return Response({"data": serializers.data, "status": status.HTTP_200_OK})
#
# @api_view(["PUT"])
# def sumka_update_put(request,pk):
#     sumka = Sumka.objects.get(id=pk)
#     serializers = Sumkaserializers(sumka,data=request.data)
#     if serializers.is_valid():
#         serializers.save()
#         return Response({"data": serializers.data, "status": status.HTTP_200_OK})
#     return Response({"data": serializers.data, "status": status.HTTP_400_BAD_REQUEST})
#
# @api_view(["PATCH"])
# def sumka_update_patch(request,pk):
#     sumka = Sumka.objects.get(id=pk)
#     serializers = Sumkaserializers(sumka,data=request.data,partial=True)
#     if serializers.is_valid():
#         serializers.save()
#         return Response({"data": serializers.data, "status": status.HTTP_200_OK})
#     return Response({"data": serializers.data, "status": status.HTTP_400_BAD_REQUEST})
#
# @api_view(["DELETE"])
# def sumka_delete(request,pk):
#     sumka = Sumka.objects.get(id=pk)
#     sumka.delete()
#     return Response(status=status.HTTP_200_OK)
# <------------------------------------------------------------------------->
