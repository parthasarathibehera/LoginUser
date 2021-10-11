from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from app.serializer import EmployeeSerializer, EmployeeModel
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.generics import CreateAPIView


class IndexPage(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        return Response()


class CreateUser(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'create_user.html'

    def get(self, request):
        return Response()


class SaveUser(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
        return Response()


class LoginUser(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'all_user.html'

    def post(self, request):
        queryset = EmployeeModel.objects.all()
        return Response({"data": queryset})


class Logout(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        return Response()