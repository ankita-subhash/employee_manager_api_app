from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view, renderer_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from api.serializers import EmpInfoSerializer
from staff.models import EmpInfo
import coreapi
from rest_framework.schemas import AutoSchema
from rest_framework_swagger import renderers as swagger_renderer
from rest_framework import renderers


@api_view()
@renderer_classes([renderers.CoreJSONRenderer,
                   swagger_renderer.OpenAPIRenderer,
                   swagger_renderer.SwaggerUIRenderer,
                   ])
def schema_view(request):
    api_schema = api_schema_generator()
    return response.Response(api_schema)

@api_view(['GET'])
def emplist(request):
    emplist = EmpInfo.objects.all()
    serializers = EmpInfoSerializer(emplist, many = True)
    return Response(serializers.data)


@api_view(['GET'])
def empview(request, pk):
    emplist = EmpInfo.objects.get(id=pk)
    serializers = EmpInfoSerializer(emplist, many = False)
    return Response(serializers.data)

@csrf_exempt
@api_view(['POST'])
def addemp(request):
    serializers = EmpInfoSerializer(data = request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data, status = 201 )

@csrf_exempt
@api_view(['PUT'])
def updateemp(request, pk):
    emplist = EmpInfo.objects.get(id=pk)
    serializers = EmpInfoSerializer(data = request.data, instance = emplist)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)


@api_view(['DELETE'])
def deleteemp(request, pk):
    emplist = EmpInfo.objects.get(id=pk)
    emplist.delete()
    return Response('Data Deleted')
